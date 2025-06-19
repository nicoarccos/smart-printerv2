# red_impresora.py

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


async def obtener_ips(ip, community):
    base_oid = "1.3.6.1.2.1.4.20.1.1"  # IP-MIB::ipAdEntAddr
    engine = SnmpEngine()
    transport = await UdpTransportTarget.create((ip, 161))
    community_data = CommunityData(community, mpModel=1)
    context = ContextData()

    current_oid = ObjectType(ObjectIdentity(base_oid))
    direcciones_ip = []

    while True:
        errorIndication, errorStatus, errorIndex, varBinds = await next_cmd(
            engine,
            community_data,
            transport,
            context,
            current_oid,
            lexicographicMode=False
        )

        if errorIndication or errorStatus or not varBinds:
            break

        for varBind in varBinds:
            oid, value = varBind
            if not str(oid).startswith(base_oid):
                return direcciones_ip

            ip_str = value.prettyPrint()
            if ip_str != "127.0.0.1":
                direcciones_ip.append(ip_str)

            current_oid = ObjectType(ObjectIdentity(str(oid)))

    return direcciones_ip


async def verificar_estado_snmp(ip, community):
    test_oid = "1.3.6.1.2.1.1.5.0"  # Nombre del host
    valor = await obtener_valor(ip, community, test_oid)
    return "Online" if valor else "Offline"


async def obtener_info_red(ip, community):
    direcciones = await obtener_ips(ip, community)
    estado = await verificar_estado_snmp(ip, community)

    return {
        "DireccionIP": direcciones[0] if direcciones else "N/A",
        "Estado": estado
    }


# Para ejecutar directamente este módulo
if __name__ == '__main__':
    async def main():
        resultado = await obtener_info_red("192.168.223.1", "public")
        import json
        print(json.dumps(resultado, indent=4))

    asyncio.run(main())
