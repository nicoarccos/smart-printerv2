from qdarkstyle import load_stylesheet_pyside6
from ui.escaneo_window import Escaneo
from ui.alarmas_window import AlarmaWidget
from ui.tabla_impresoras import TablaImpresoras

from core.monitor_manager import MonitorManager
from ui.notificaciones_window import Notificaciones
from utils.utils import abs_path

import sys
from ui.mainwindow import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Instanciar vistas en paginas de StackedWidget
        self.tabla_impresoras = TablaImpresoras()
        self.alarma_widget = AlarmaWidget()
        self.notificaciones_widget = Notificaciones()
        self.escaneo_widget = Escaneo(self.tabla_impresoras, self.stackedWidget)

        self.monitor = MonitorManager()

        # Agregar vistas a StackedWidget
        self.stackedWidget.addWidget(self.tabla_impresoras)
        self.stackedWidget.addWidget(self.alarma_widget)
        self.stackedWidget.addWidget(self.notificaciones_widget)
        self.stackedWidget.addWidget(self.escaneo_widget)

        # Conectar vistas con click en boton
        self.escaneo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.escaneo_widget))
        #self.escaneo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.tabla_impresoras))
        self.alarmas.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.alarma_widget))
        self.notificaciones.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.notificaciones_widget))
#        self.escaneo_widget.set_parent_widget(self.stackedWidget)

    #Carga de estilos
    def cargarQSS(self, fichero):
        path = abs_path(fichero)
        try:
            with open(path) as styles:
                self.setStyleSheet(styles.read())
        except:
            print("Erorr abirnedo los estilos",path)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(load_stylesheet_pyside6())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())