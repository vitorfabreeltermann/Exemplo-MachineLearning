# coding=utf-8
import pandas as pd
import nltk
import numpy as np

from Executador import Executador

def main():
    X, Y = ler_csv()
    executador = Executador()
    executador.executar(X, Y, 0.9, 10)

def ler_csv():
    classificacoes = pd.read_csv('emails.csv', encoding='utf-8')
    textosPuros = classificacoes['email']
    frases = textosPuros.str.lower()
    # nltk.download('punkt')
    textosQuebrados = [nltk.tokenize.word_tokenize(frase) for frase in frases]
    dicionario = set()

    # nltk.download('stopwords')
    stopwords = nltk.corpus.stopwords.words("portuguese")

    # nltk.download('rslp')
    stemmer = nltk.stem.RSLPStemmer()

    for lista in textosQuebrados:
        validas = [stemmer.stem(palavra) for palavra in lista if palavra not in stopwords and len(palavra) > 2]
        dicionario.update(validas)

    totalDePalavras = len(dicionario)
    tuplas = list(zip(dicionario, range(totalDePalavras)))
    tradutor = {palavra: indice for palavra, indice in tuplas}

    def vetorizar_texto(texto, tradutor):
        vetor = [0] * len(tradutor)

        for palavra in texto:
            if len(palavra) > 0:
                raiz = stemmer.stem(palavra)
                if raiz in tradutor:
                    posicao = tradutor[raiz]
                    vetor[posicao] += 1
        return vetor

    vetoresDeTexto = [vetorizar_texto(texto, tradutor) for texto in textosQuebrados]
    marcas = classificacoes['classificacao']

    X = np.array(vetoresDeTexto)
    Y = np.array(marcas.tolist())

    return X, Y


main()