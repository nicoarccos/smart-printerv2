# tabla_impresoras.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem

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
        self.tabla.setColumnCount(7)
        self.tabla.setHorizontalHeaderLabels([
            "Impresora", "IP", "Estado", "Tinta", "Contador", "Ultimo Escaneo", "Ubicacion"
        ])

    def cargar_datos(self):
        datos = [
            {"Impresora": "Epson", "IP": "192.165.231.31", "Estado": "Activa", "Tinta": "50%",
             "Contador": "534", "Ultimo Escaneo": "25-3:25 12:30:22", "Ubicacion": "Sistemas"},
            {"Impresora": "HP", "IP": "192.165.134.31", "Estado": "Activa", "Tinta": "23%",
             "Contador": "12", "Ultimo Escaneo": "25-3:25 12:30:22", "Ubicacion": "Finanzas"}
        ]

        self.tabla.setRowCount(len(datos))

        for fila, item in enumerate(datos):
            self.tabla.setItem(fila, 0, QTableWidgetItem(item["Impresora"]))
            self.tabla.setItem(fila, 1, QTableWidgetItem(item["IP"]))
            self.tabla.setItem(fila, 2, QTableWidgetItem(item["Estado"]))
            self.tabla.setItem(fila, 3, QTableWidgetItem(item["Tinta"]))
            self.tabla.setItem(fila, 4, QTableWidgetItem(item["Contador"]))
            self.tabla.setItem(fila, 5, QTableWidgetItem(item["Ultimo Escaneo"]))
            self.tabla.setItem(fila, 6, QTableWidgetItem(item["Ubicacion"]))
