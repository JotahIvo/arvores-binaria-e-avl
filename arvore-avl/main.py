from noh_arvore_avl import NohArvoreAVL


def imprimir_arvore(arvore, nivel=0, prefixo='Raiz: '):
    if arvore is not None:
        print(' ' * (nivel * 4) + prefixo + str(arvore.info))
        if arvore.esquerda is not None or arvore.direita is not None:
            imprimir_arvore(arvore.esquerda, nivel + 1, 'ESQ: ')
            imprimir_arvore(arvore.direita, nivel + 1, 'DIR: ')


def retorna_altura(noh):
    if noh is None:
        return 0
    return noh.altura


def balanco(noh):
    if noh is None:
        return 0
    return retorna_altura(noh.esquerda) - retorna_altura(noh.direita)


#criando uma arvore avl já balanceada:
raiz = NohArvoreAVL(4, 3)
raiz.esquerda = NohArvoreAVL(2, 2)
raiz.direita = NohArvoreAVL(6, 2)
raiz.esquerda.esquerda = NohArvoreAVL(1, 1)
raiz.esquerda.direita = NohArvoreAVL(3, 1)
raiz.direita.esquerda = NohArvoreAVL(5, 1)
raiz.direita.direita = NohArvoreAVL(7, 1)

raiz_nao_balanceada = NohArvoreAVL(1, 3)
raiz_nao_balanceada.direita = NohArvoreAVL(2, 2)
raiz_nao_balanceada.direita.direita = NohArvoreAVL(3, 1)

imprimir_arvore(raiz)
print("O fator de balandeamento da raiz é: ", balanco(raiz), "\n")
imprimir_arvore(raiz_nao_balanceada)
print("O fator de balandeamento da raiz é: ", balanco(raiz_nao_balanceada), "\n")
