# coding=utf-8

from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsOneClassifier
from sklearn.naive_bayes import MultinomialNB

from Algoritmo import Algoritmo
from Treinador import Treinador
from Validador import Validador

class Executador:

    def executar(self, X, Y, porcentagem_de_treino, k):

        tamanho_do_treino = int(porcentagem_de_treino * len(Y))
        # tamanho_de_validacao = len(Y) - tamanho_do_treino

        treino_dados, validacao_dados = self.__separar(X, tamanho_do_treino)
        treino_marcacoes, validacao_marcacoes = self.__separar(Y, tamanho_do_treino)

        algoritmo_one_vs_one = Algoritmo("OneVsOne", OneVsRestClassifier(LinearSVC(random_state=0)))
        algoritmo_one_vs_rest = Algoritmo("OneVsRest", OneVsOneClassifier(LinearSVC(random_state=0)))
        algoritmo_multinomial = Algoritmo("Multinomial", MultinomialNB())
        treinador = Treinador() \
            .add_algoritmo(algoritmo_one_vs_one) \
            .add_algoritmo(algoritmo_one_vs_rest) \
            .add_algoritmo(algoritmo_multinomial)
        resultados = treinador.treinar(treino_dados, treino_marcacoes, k)

        vencedor = self.__calcula_vencedor(resultados)
        print("Vencerdor: {0}".format(vencedor.algoritmo.nome))

        vencedor.algoritmo.fit(treino_dados, treino_marcacoes)
        vencedor.algoritmo.teste_real(validacao_dados, validacao_marcacoes)

        validador = Validador()
        validador.validar(validacao_marcacoes, validacao_dados)

    def __separar(self, A, tamanho_do_treino):
        treino = A[0:tamanho_do_treino]
        validacao = A[tamanho_do_treino:]

        return treino, validacao

    def __calcula_vencedor(self, resultados):
        vencedor = None
        for resultado in resultados:
            if vencedor == None or resultado.resultado > vencedor.resultado:
                vencedor = resultado
        return vencedor
