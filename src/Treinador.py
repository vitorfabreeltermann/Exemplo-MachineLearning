#from . import Algoritmo
from Resultado import Resultado

class Treinador:

    def __init__(self):
        self.__algoritmos = []

    def treinar(self, dados, marcacoes, k):
        resultados = []
        for algoritmo in self.__algoritmos:
            res = algoritmo.fit_and_predict(dados, marcacoes, k)
            resultado = Resultado(algoritmo, res)

            resultados.append(resultado)


        return resultados

    def add_algoritmo(self, algoritmo):
        self.__algoritmos.append(algoritmo)
        return self