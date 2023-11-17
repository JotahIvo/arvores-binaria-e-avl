from noh_arvore import NohArvore
from arvore_binaria import *

raiz = NohArvore(40)
for chave in [20, 60, 50, 70, 10, 30]:
    noh = NohArvore(chave)
    insere_noh(raiz, noh)

raiz_compara = NohArvore(40)
for chave in [20, 60, 50, 70, 10, 30]:
    noh = NohArvore(chave)
    insere_noh(raiz_compara, noh)


def imprimir_arvore(arvore, nivel=0, prefixo='Raiz: '):
    if arvore is not None:
        print(' ' * (nivel * 4) + prefixo + str(arvore.info))
        if arvore.esquerda is not None or arvore.direita is not None:
            imprimir_arvore(arvore.esquerda, nivel + 1, 'ESQ: ')
            imprimir_arvore(arvore.direita, nivel + 1, 'DIR: ')


#em_ordem(raiz)
print(busca_arvore_binaria(raiz, 60))
print("Altura da árvore: ", altura_arvore(raiz))
print("Quantidade de nós da árvore: ", quantidade_noh_arvore(raiz))
print("Quantidade de folhas da árvore: ", quantidade_folhas_arvore(raiz))
imprimir_arvore(raiz)

print("\n Removendo o 20:\n")

#imprimir_arvore(remove_noh(raiz, 20))

print(compara_arvore_binaria(raiz, raiz_compara))