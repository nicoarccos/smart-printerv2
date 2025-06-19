import asyncio
import json
from info_host import obtener_info_sistema
from toner_model import obtener_estado_impresora
from red_impresora import *

async def generar_reporte(ip, community):
    info_sistema = await obtener_info_sistema(ip, community)
    niveles_toner = await obtener_estado_impresora(ip, community)
    info_red = await obtener_info_red(ip,community)



    resultado = {
        "InformacionDelSistema": info_sistema,
        "NivelesDeToner": niveles_toner if niveles_toner else "No disponible",
        "InformacionDeRed": info_red if info_red else "No disponible"
    }

    print(json.dumps(resultado, indent=4))

    with open("estado_impresora.json", "w") as f:
        json.dump(resultado, f, indent=4)

if __name__ == "__main__":
    asyncio.run(generar_reporte("192.168.223.1", "public"))
