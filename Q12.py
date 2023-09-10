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

    def remover(self, no_atual, valor):
        if no_atual is None:
            return no_atual
        if valor < no_atual.valor:
            no_atual.no_esquerdo = self.remover(no_atual.no_esquerdo, valor)
        elif valor > no_atual.valor:
            no_atual.no_direito = self.remover(no_atual.no_direito, valor)
        else:
            if no_atual.no_esquerdo is None:
                return no_atual.no_direito
            elif no_atual.no_direito is None:
                return no_atual.no_esquerdo
            no_atual.valor = self.encontrar_sucessor(no_atual.no_direito).valor
            no_atual.no_direito = self.remover(no_atual.no_direito, no_atual.valor)
        return no_atual

    def encontrar_sucessor(self, no_atual):
        while no_atual.no_esquerdo is not None:
            no_atual = no_atual.no_esquerdo
        return no_atual