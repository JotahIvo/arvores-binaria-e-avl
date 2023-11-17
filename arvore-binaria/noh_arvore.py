class NohArvore:
    def __init__(self, info=None, esquerda=None, direita=None):
        self.info = info
        self.esquerda = esquerda
        self.direita = direita

    
    def __repr__(self):
        return f"{self.esquerda.info} <- {self.info} -> {self.direita.info}"
