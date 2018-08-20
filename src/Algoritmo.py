#!-*- coding: utf8 -*-

from sklearn.model_selection import cross_val_score
import numpy as np


class Algoritmo:

    def __init__(self, nome, modelo):
        self.__nome = nome
        self.__modelo = modelo

    def fit_and_predict(self, dados, marcacoes, k):
        scores = cross_val_score(self.__modelo, dados, marcacoes, cv=k)
        taxa_de_acerto = np.mean(scores)
        msg = "Taxa de acerto do {0}: {1}".format(self.__nome, taxa_de_acerto)
        print(msg)
        return taxa_de_acerto

    def fit(self, dados, marcadores):
        self.__modelo.fit(dados, marcadores)

    def teste_real(self, dados, marcacoes):
        resultado = self.__modelo.predict(dados)

        acertos = resultado == marcacoes

        total_de_acertos = sum(acertos)
        total_de_elementos = len(marcacoes)

        taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

        msg = "Taxa de acerto do vencedor entre os algoritmos foi o {0} com {1}".format(self.__nome, taxa_de_acerto)
        print(msg)
        return taxa_de_acerto

    @property
    def nome(self):
        return self.__nome

    @property
    def modelo(self):
        return self.__modelo