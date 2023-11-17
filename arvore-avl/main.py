from noh_arvore_avl import No_AVL


def imprimir_arvore(arvore, nivel=0, prefixo='Raiz: '):
    if arvore is not None:
        print(' ' * (nivel * 4) + prefixo + str(arvore.data) + " - FB: " + str(arvore.balanceamento))
        if arvore.esquerda is not None or arvore.direita is not None:
            imprimir_arvore(arvore.esquerda, nivel + 1, 'ESQ: ')
            imprimir_arvore(arvore.direita, nivel + 1, 'DIR: ')


arvore_avl = No_AVL(1)

arvore_avl.insere(2)
arvore_avl.insere(3)
arvore_avl.insere(4)
arvore_avl.insere(5)
arvore_avl.insere(6)
arvore_avl.insere(7)

imprimir_arvore(arvore_avl)
