"""
    UFRJ - Universidade Federal do Rio de Janeiro
    MAE015 - Tóp. Especiais em Engenharia de dados A: Estrutura de dados

    Autores:
        Nome: Rhuan Justo
        DRE: 118043398

        Nome: Davi RIchards
        DRE: 119022078

        Nome: Sebastião Rodrigo
        DRE: 117099621

        Nome: Yuri Ferreira Melo
        DRE: 120081378
"""

class No:

    def __init__(self, key: int) -> None:
        self.key = key
        self.filhoEsquerda = None    
        self.filhoDireita = None
        self.altura = 1

class ArvoreAVL:

    def __init__(self) -> None:
        self.raiz = No(None)


    def inserir(self, key: int) -> None:
        novo = No(key)
        if self.raiz == None:
            self.raiz = novo
        elif key < self.raiz.key:
            self.raiz.filhoEsquerda = self.inserir(self.raiz.filhoEsquerda, key)
        else:
            self.raiz.filhoDireita = self.inserir(self.raiz.filhoDireita, key)

    def getAltura(self) -> None:
        pass

    def rotacaoEsquerda(self) -> None:
        pass

    def rotacaoDireita(self) -> None:
        pass
