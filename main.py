from ui.mainwindow import Ui_MainWindow
from utils.utils import abs_path
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.mainwindow import Ui_MainWindow
import sys
import os
from ui.mainwindow import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.cargarQSS("assets/qss/QDark.qss")
        #posibles
        #Dtor
        #MailSy
        #QDark
        #QDarkOrange

        self.cargar_datos_tabla()

    #Carga de estilos
    def cargarQSS(self, fichero):
        path = abs_path(fichero)
        try:
            with open(path) as styles:
                self.setStyleSheet(styles.read())
        except:
            print("Erorr abirnedo los estilos",path)


    # Conexion entre botones y paginas de stacked widget
        self.escaneo.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.alarmas.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.notificaciones.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.informacion.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.salir.clicked.connect(lambda: self.close())

    def cargar_datos_tabla(self):
        # Lista hipotetica de prueba para visualizacion
        datos_metricas = [
            {"Impresora": "Epson", "IP": "192.165.231.31","Estado": "Activa", "Tinta": "50%", "Contador": "534", "Ultimo Escaneo": "25-3:25 12:30:22", "Ubicacion": "Sistemas"},
            {"Impresora": "HP", "IP": "192.165.134.31", "Estado": "Activa", "Tinta": "23%", "Contador": "12","Ultimo Escaneo": "25-3:25 12:30:22", "Ubicacion": "Finanzas"}

        ]

        # Configuracion de tabla (numero de filas y columnas)
        self.tableWidget.setRowCount(len(datos_metricas))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["Impresora", "IP", "Estado", "Tinta", "Contador", "Ultimo Escaneo", "Ubicacion"])

        # Llenamos la tabla con datos
        for fila, datos in enumerate(datos_metricas):
            self.tableWidget.setItem(fila, 0, QTableWidgetItem(datos["Impresora"]))
            self.tableWidget.setItem(fila, 1, QTableWidgetItem(datos["IP"]))
            self.tableWidget.setItem(fila, 2, QTableWidgetItem(datos["Estado"]))
            self.tableWidget.setItem(fila, 3, QTableWidgetItem(datos["Tinta"]))
            self.tableWidget.setItem(fila, 4, QTableWidgetItem(datos["Contador"]))
            self.tableWidget.setItem(fila, 5, QTableWidgetItem(datos["Ultimo Escaneo"]))
            self.tableWidget.setItem(fila, 6, QTableWidgetItem(datos["Ubicacion"]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())