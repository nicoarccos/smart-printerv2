# estado_impresora.py

import asyncio
from pysnmp.hlapi.asyncio import *

async def obtener_valor(ip, community, oid):
    engine = SnmpEngine()
    transport = await UdpTransportTarget.create((ip, 161))
    community_data = CommunityData(community, mpModel=1)
    context = ContextData()

    errorIndication, errorStatus, errorIndex, varBinds = await get_cmd(
        engine,
        community_data,
        transport,
        context,
        ObjectType(ObjectIdentity(oid))
    )

    if errorIndication or errorStatus:
        return None

    for varBind in varBinds:
        return str(varBind[1])
    return None

def interpretar_estado_dispositivo(estado):
    estados = {
        "1": "unknown",
        "2": "running",
        "3": "idle",
        "4": "printing",
        "5": "warmup"
    }
    return estados.get(str(estado), "desconocido")

def interpretar_estado_toner(valor):
    estados = {
        "0": "OK",
        "1": "Otro",
        "2": "Desconocido",
        "3": "Bajo",
        "4": "Vacío"
    }
    return estados.get(str(valor), "desconocido")

async def obtener_estado_impresora(ip, community):
    modelo_oid = "1.3.6.1.2.1.25.3.2.1.3.1"
    estado_dispositivo_oid = "1.3.6.1.2.1.25.3.2.1.5.1"
    nivel_toner_negro_oid = "1.3.6.1.2.1.43.11.1.1.8.1.1"
    estado_toner_negro_oid = "1.3.6.1.2.1.43.11.1.1.9.1.1"
    paginas_impresas_oid = "1.3.6.1.2.1.43.10.2.1.4.1.1"

    modelo = await obtener_valor(ip, community, modelo_oid)
    estado_dispositivo = await obtener_valor(ip, community, estado_dispositivo_oid)
    nivel_toner = await obtener_valor(ip, community, nivel_toner_negro_oid)
    estado_toner = await obtener_valor(ip, community, estado_toner_negro_oid)
    paginas_impresas = await obtener_valor(ip, community, paginas_impresas_oid)

    return {
        "ModeloDeImpresora": modelo if modelo else "N/A",
        "EstadoDelDispositivo": interpretar_estado_dispositivo(estado_dispositivo) if estado_dispositivo else "N/A",
        "NivelDeTonerNegro": f"{nivel_toner}%" if nivel_toner else "N/A",
        "EstadoTonerNegro": interpretar_estado_toner(estado_toner) if estado_toner else "N/A",
        "PaginasImpresas": paginas_impresas if paginas_impresas else "N/A"
    }

# Para pruebas individuales:
if __name__ == "__main__":
    async def main():
        estado = await obtener_estado_impresora("192.168.223.1", "public")
        from pprint import pprint
        pprint(estado)
    asyncio.run(main())
