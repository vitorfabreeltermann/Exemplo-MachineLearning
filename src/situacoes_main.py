# coding=utf-8
import pandas as pd
from Executador import Executador

def main():
    X, Y = ler_csv()
    executador = Executador()
    executador.executar(X, Y, 0.9, 10)

def ler_csv():
    df = pd.read_csv('situacao_do_cliente.csv')
    X_df = df[['recencia', 'frequencia', 'semanas_de_inscricao']]
    Y_df = df['situacao']

    Xdummies_df = pd.get_dummies(X_df)
    Ydummies_df = Y_df

    X = Xdummies_df.values
    Y = Ydummies_df.values

    return X, Y


main()