import asyncio
import json
from agent.info_host import *
from agent.red_impresora import *
from agent.toner_model import *
from pathlib import Path

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

    ruta_json = Path(__file__).resolve().parent / "estado_impresora.json"
    with open(ruta_json, "w", encoding="utf-8") as f:
        json.dump(resultado, f, indent=4)
if __name__ == "__main__":
    asyncio.run(generar_reporte("192.168.223.1", "public"))
