def altura_arvore(noh):
        if noh is None:
            return 0
        return noh.altura


def fator_balanceamento(noh):
    if noh is None:
        return 0
    return altura_arvore(noh.esquerda) - altura_arvore(noh.direita)