# tabla_impresoras.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
import json
from datetime import datetime
from pathlib import Path


class TablaImpresoras(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        self.tabla = QTableWidget()
        layout.addWidget(self.tabla)
        self.setLayout(layout)

        self.configurar_tabla()
        self.cargar_datos()

    def configurar_tabla(self):
        self.tabla.setColumnCount(8)
        self.tabla.setHorizontalHeaderLabels([
            "Host", "Modelo", "IP", "Estado", "Tinta", "Contador", "Ultimo Escaneo", "Ubicacion"
        ])

    def cargar_datos(self):
        ruta_json = Path(__file__).resolve().parent.parent / "agent" / "estado_impresora.json"

        if not ruta_json.exists():
            print("⚠️ Archivo JSON no encontrado.")
            return

        with open(ruta_json, "r", encoding="utf-8") as f:
            datos_json = json.load(f)

        datos = [{
            "Host": datos_json["InformacionDelSistema"].get("NombreDelHost", "N/A"),
            "Modelo": datos_json["NivelesDeToner"].get("Modelo", "N/A"),
            "IP": datos_json["InformacionDeRed"].get("DireccionIP", "N/A"),
            "Estado": datos_json["InformacionDeRed"].get("Estado", "N/A"),
            "Tinta": datos_json["NivelesDeToner"].get("NivelToner", "N/A"),
            "Contador": datos_json["NivelesDeToner"].get("PaginasTotales", "N/A"),
            "Ultimo Escaneo": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            "Ubicacion": "Desconocida"
        }]

        self.tabla.setRowCount(len(datos))

        for fila, item in enumerate(datos):
            self.tabla.setItem(fila, 0, QTableWidgetItem(item["Host"]))
            self.tabla.setItem(fila, 1,QTableWidgetItem(item["Modelo"]))
            self.tabla.setItem(fila, 2, QTableWidgetItem(item["IP"]))
            self.tabla.setItem(fila, 3, QTableWidgetItem(item["Estado"]))
            self.tabla.setItem(fila, 4, QTableWidgetItem(item["Tinta"]))
            self.tabla.setItem(fila, 5, QTableWidgetItem(item["Contador"]))
            self.tabla.setItem(fila, 6, QTableWidgetItem(item["Ultimo Escaneo"]))
            self.tabla.setItem(fila, 7, QTableWidgetItem(item["Ubicacion"]))

    def actualizar_tabla(self):
        try:
            ruta_json = Path(__file__).resolve().parent.parent / "agent" / "estado_impresora.json"
            with open(ruta_json, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"❌ Error leyendo el JSON: {e}")
            return

        self.tabla.setRowCount(1)

        self.tabla.setItem(0, 0, QTableWidgetItem(data["InformacionDelSistema"].get("NombreDelHost", "N/A")))
        self.tabla.setItem(0, 1, QTableWidgetItem(data["NivelesDeToner"].get("Modelo", "N/A")))
        self.tabla.setItem(0, 2, QTableWidgetItem(data["InformacionDeRed"].get("DireccionIP", "N/A")))
        self.tabla.setItem(0, 3, QTableWidgetItem(data["InformacionDeRed"].get("Estado", "N/A")))
        self.tabla.setItem(0, 4, QTableWidgetItem(data["NivelesDeToner"].get("NivelToner", "N/A")))
        self.tabla.setItem(0, 5, QTableWidgetItem(data["NivelesDeToner"].get("PaginasTotales", "N/A")))
        self.tabla.setItem(0, 6, QTableWidgetItem(datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
        self.tabla.setItem(0, 7, QTableWidgetItem("Desconocida"))

