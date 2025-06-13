#Orquestacion de los escaneos en paralelos


from PySide6.QtCore import QObject, QThreadPool
from core.escaneo_worker import EscaneoWorker

class MonitorManager(QObject):
    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool()

    def escanear_ips(self, lista_ips, callback):
        for ip in lista_ips:
            worker = EscaneoWorker(ip)
            worker.signals.resultado.connect(callback)
            self.threadpool.start(worker)
