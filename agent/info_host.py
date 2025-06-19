# info_sistema.py

import asyncio
from pysnmp.hlapi.asyncio import *

def convertir_timeticks(timeticks):
    segundos = int(timeticks) // 100
    dias = segundos // 86400
    horas = (segundos % 86400) // 3600
    minutos = (segundos % 3600) // 60
    segundos = segundos % 60
    return f"{dias}d {horas}h {minutos}m {segundos}s"

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

async def obtener_info_sistema(ip, community):
    nombre_host_oid = "1.3.6.1.2.1.1.5.0"
    tiempo_actividad_oid = "1.3.6.1.2.1.1.3.0"

    nombre_host = await obtener_valor(ip, community, nombre_host_oid)
    tiempo_timeticks = await obtener_valor(ip, community, tiempo_actividad_oid)

    return {
        "NombreDelHost": nombre_host if nombre_host else "N/A",
        "TiempoDeActividad": convertir_timeticks(tiempo_timeticks) if tiempo_timeticks else "N/A"
    }

# Para pruebas individuales:
if __name__ == "__main__":
    async def main():
        data = await obtener_info_sistema("192.168.223.1", "public")
        print(data)
    asyncio.run(main())