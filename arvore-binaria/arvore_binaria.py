#funções para árvores binárias:

def em_ordem(raiz):
    if not raiz:
        return 

    em_ordem(raiz.esquerda)

    print(raiz.info)

    em_ordem(raiz.direita)


def encontra_menor_valor(raiz):
    while raiz.esquerda is not None:
        raiz = raiz.esquerda

    return raiz


def insere_noh(raiz, noh):
    if raiz is None:
        raiz = noh
    elif raiz.info < noh.info:
        if raiz.direita is None:
            raiz.direita = noh
        else:
            insere_noh(raiz.direita, noh)
    else:
        if raiz.esquerda is None:
            raiz.esquerda = noh
        else:
            insere_noh(raiz.esquerda, noh)


def busca_arvore_binaria(raiz, valor):
    if raiz is None:
        return None

    if raiz.info == valor:
        return raiz

    if valor < raiz.info:
        return busca_arvore_binaria(raiz.esquerda, valor)

    if valor > raiz.info:
        return busca_arvore_binaria(raiz.direita, valor)


#questão 1
def remove_noh(raiz, valor):
    if raiz is None:
        return raiz

    if raiz.info > valor:
        raiz.esquerda = remove_noh(raiz.esquerda, valor)
    elif raiz.info < valor:
        raiz.direita = remove_noh(raiz.direita, valor)
    else:
        if raiz.esquerda is None:
            return raiz.direita
        elif raiz.direita is None:
            return raiz.esquerda

        raiz.info = encontra_menor_valor(raiz.direita).info
        raiz.direita = remove_noh(raiz.direita, raiz.info)

    return raiz


#questão 2 
def altura_arvore(raiz):
    if raiz is None:
        return 0

    return max(altura_arvore(raiz.esquerda), altura_arvore(raiz.direita)) + 1


#questão 3 
def quantidade_noh_arvore(raiz):
    if raiz is None:
        return 0
    
    return 1 + quantidade_noh_arvore(raiz.esquerda) + quantidade_noh_arvore(raiz.direita)
    

#questão 4
def quantidade_folhas_arvore(raiz):
    if raiz is None:
        return 0
    elif raiz.esquerda is None and raiz.direita is None:
        return 1
    
    return quantidade_folhas_arvore(raiz.esquerda) + quantidade_folhas_arvore(raiz.direita)


#questão 5
def compara_arvore_binaria(raiz, raiz_compara):
    if raiz is None and raiz_compara is None:
        return True

    if raiz is not None and raiz_compara is not None:
        if raiz.info == raiz_compara.info and compara_arvore_binaria(raiz.esquerda, raiz_compara.esquerda) and compara_arvore_binaria(raiz.direita, raiz_compara.direita):
            return True

    return False

