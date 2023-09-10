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

    def caminho_no(arvore, valor_alvo):
        def busca_caminho(no, valor_alvo, caminho_atual):
            if no is None:
                return None
            caminho_atual.append(no.valor)
            if no.valor == valor_alvo:
                return caminho_atual.copy()
            if (busca_caminho(no.no_esquerdo, valor_alvo, caminho_atual.copy()) or
                    busca_caminho(no.no_direito, valor_alvo, caminho_atual.copy())):
                return caminho_atual.copy()
            caminho_atual.pop()
            return None
        caminho = busca_caminho(arvore, valor_alvo, [])
        return caminho