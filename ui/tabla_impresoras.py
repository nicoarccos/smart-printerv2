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
            "Modelo": datos_json["NivelesDeToner"].get("ModeloDeImpresora", "N/A"),
            "IP": datos_json["InformacionDeRed"].get("DireccionIP", "N/A"),
            "Estado": datos_json["InformacionDeRed"].get("Estado", "N/A"),
            "Tinta": datos_json["NivelesDeToner"].get("NivelDeTonerNegro", "N/A"),
            "Contador": datos_json["NivelesDeToner"].get("PaginasImpresas", "N/A"),
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


