from PySide6.QtCore import QObject, Signal, QRunnable
import subprocess
import platform

class EscaneoSeniales(QObject):
    resultado = Signal(str, bool) #IP, estado (True=en linea, False=apagada)


class EscaneoWorker(QRunnable):
    def __init__(self, ip):
        super().__init__()
        self.ip = ip #recibe ip a escanear
        self.signals = EscaneoSeniales() # crea su propia señal

    def run(self):
        parametro = "-n" if platform.system().lower() == "windows" else "-c" # comando a ejecutar en windows o linux
        comando = ["ping", parametro, "1", self.ip] # arma el comando de ping en forma de lista

        try:
            resultado = subprocess.run(comando, stdout=subprocess.DEVNULL) # ejecuta el ping, descarta la salida stdout enviandola a DEVNULL
            conectado = resultado.returncode == 0 # codigo de salida igual a 0? exitoso
        except Exception:
            conectado = False
        self.signals.resultado.emit(self.ip, conectado) # emision de señal con resultado de codigo de salida.

