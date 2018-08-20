from collections import Counter

class Validador:

    def validar(self, validacao_marcacoes, validacao_dados):
        acerto_base = max(Counter(validacao_marcacoes).values())
        taxa_de_acerto_base = 100.0 * acerto_base / len(validacao_marcacoes)
        print("Taxa de acerto base: %f" % taxa_de_acerto_base)

        total_de_elementos = len(validacao_dados)
        print("Total de teste: %d" % total_de_elementos)