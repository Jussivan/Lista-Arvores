class No:
    def __init__(self, valor):
        self.valor = valor
        self.no_esquerdo = None
        self.no_direito = None

class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self.inserir_recursivo(self.raiz, valor)

    def inserir_recursivo(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.no_esquerdo is None:
                no_atual.no_esquerdo = No(valor)
            else:
                self.inserir_recursivo(no_atual.no_esquerdo, valor)
        elif valor > no_atual.valor:
            if no_atual.no_direito is None:
                no_atual.no_direito = No(valor)
            else:
                self.inserir_recursivo(no_atual.no_direito, valor)

    def contar_nos(arvore):
        if arvore is None:
            return 0
        else:
            return 1 + contar_nos(arvore.no_esquerdo) + contar_nos(arvore.no_direito)