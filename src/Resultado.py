#from . import Algoritmo
#from . import Resultado

class Resultado:

    def __init__(self, algoritmo, resultado):
        self.__algoritmo = algoritmo
        self.__resultado = resultado

    @property
    def algoritmo(self):
        return self.__algoritmo

    @property
    def resultado(self):
        return self.__resultado

    def a(self):
        print("jsijfisjsdi")