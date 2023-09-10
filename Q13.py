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

    def nos_em_nivel(arvore, nivel_desejado):
        if arvore is None or nivel_desejado < 1:
            return []
        fila = [(arvore, 1)]
        nos_no_nivel = []
        while fila:
            no_atual, nivel_atual = fila.pop(0)
            if nivel_atual == nivel_desejado:
                nos_no_nivel.append(no_atual.valor)
            if nivel_atual < nivel_desejado:
                if no_atual.no_esquerdo:
                    fila.append((no_atual.no_esquerdo, nivel_atual + 1))
                if no_atual.no_direito:
                    fila.append((no_atual.no_direito, nivel_atual + 1))
        return nos_no_nivel