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

    def busca_valida(arvore):
        def travessia_inordem_valida(no, valores):
            if no is None:
                return True
            if not travessia_inordem_valida(no.no_esquerdo, valores):
                return False
            if valores[0] is not None and no.valor <= valores[0]:
                return False
            valores[0] = no.valor
            return travessia_inordem_valida(no.no_direito, valores)
        valores_anteriores = [None]
        return travessia_inordem_valida(arvore, valores_anteriores)