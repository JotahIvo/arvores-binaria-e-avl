class No_AVL:
    def __init__(self, data):
        self.data = data
        self.seta_filhos(None, None)
        self.altura_no = self.altura()
        self.balanceamento = self.fator_de_balanceamento()

    def seta_filhos(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita


    def fator_de_balanceamento(self):
        h_esq = 0
        if self.esquerda:
            h_esq = self.esquerda.altura()
        h_dir = 0
        if self.direita:
            h_dir = self.direita.altura()
        return h_esq - h_dir


    def altura(self):
        h_esq = 0
        if self.esquerda:
            h_esq = self.esquerda.altura()
        h_dir = 0
        if self.direita:
            h_dir = self.direita.altura()
        return 1 + max(h_esq, h_dir)


    def rotacao_esquerda(self):
        self.data, self.direita.data = self.direita.data, self.data
        old_esquerda = self.esquerda
        self.seta_filhos(self.direita, self.direita.direita)
        self.esquerda.seta_filhos(old_esquerda, self.esquerda.esquerda)

    def rotacao_direita(self):
        self.data, self.esquerda.data = self.esquerda.data, self.data
        old_direita = self.direita
        self.seta_filhos(self.esquerda.esquerda, self.esquerda)
        self.direita.seta_filhos(self.direita.direita, old_direita)

    def rotacao_esquerda_direita(self):
        self.esquerda.rotacao_esquerda()
        self.rotacao_direita()

    def rotacao_direita_esquerda(self):
        self.direita.rotacao_direita()
        self.rotacao_esquerda()


    def executa_fator_de_balanceamento(self):
        bal = self.fator_de_balanceamento()
        if bal > 1:
            if self.esquerda.fator_de_balanceamento() > 0:
                self.rotacao_direita()
            else:
                self.rotacao_esquerda_direita()
        elif bal < -1:
            if self.direita.fator_de_balanceamento() < 0:
                self.rotacao_esquerda()
            else:
                self.rotacao_direita_esquerda()


    def insere(self, data):
        if data <= self.data:
            if not self.esquerda:
                self.esquerda = No_AVL(data)
            else:
                self.esquerda.insere(data)
        else:
            if not self.direita:
                self.direita = No_AVL(data)
            else:
                self.direita.insere(data)
        self.executa_fator_de_balanceamento()
