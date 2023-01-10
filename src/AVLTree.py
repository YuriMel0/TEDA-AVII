'''UFRJ - Universidade Federal do Rio de Janeiro
MAE015 - Tóp. Especiais em Engenharia de dados A: Estrutura de dados
Autores:
Nome: Rhuan Justo
DRE: 118043398

Nome: Davi Richards
DRE: 119022078

Nome: Sebastião Rodrigo
DRE: 117099621

Nome: Yuri Ferreira Melo
DRE: 120081378'''

class NodoArvore:
    def __init__(self, ind, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita
        self.altura = 1.0
        self.ind = ind

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,self.chave,self.direita and self.direita.chave)

class AVLTree(object):
  def insert_node(self, root, key, ind):
        # Encontra o nó correto por recursão e adiciona a chave, guardando o índice
        if not root:
            return NodoArvore(ind,key)
        elif key < root.chave:
            root.esquerda = self.insert_node(root.esquerda, key, ind)
        else:
            root.direita = self.insert_node(root.direita, key, ind)

        root.altura= 1 + max(self.getAltura(root.esquerda),
                              self.getAltura(root.direita))

        # Atualiza o fator de balanceamento e faz o balanceamento da árvore
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key < root.esquerda.chave:
                return self.rightRotate(root)
            else:
                root.esquerda = self.leftRotate(root.esquerda)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if key > root.direita.chave:
                return self.leftRotate(root)
            else:
                root.direita = self.rightRotate(root.direita)
                return self.leftRotate(root)

        return root

    # Função para realizar a rotação à esquerda
  def leftRotate(self, z):
        y = z.direita
        T2 = y.esquerda
        y.esquerda = z
        z.direita = T2
        z.altura = 1 + max(self.getAltura(z.esquerda),
                           self.getAltura(z.direita))
        y.altura = 1 + max(self.getAltura(y.esquerda),
                           self.getAltura(y.direita))
        return y

    # Função para realizar a rotação à direita
  def rightRotate(self, z):
        y = z.esquerda
        T3 = y.direita
        y.direita = z
        z.esquerda = T3
        z.altura = 1 + max(self.getAltura(z.esquerda),
                           self.getAltura(z.direita))
        y.altura = 1 + max(self.getAltura(y.esquerda),
                           self.getAltura(y.direita))
        return y

    # Altura do nó
  def getAltura(self, root):
        if not root:
            return 0
        return root.altura

    # Fator de balanceamento do nó
  def getBalance(self, root):
        if not root:
            return 0
        return self.getAltura(root.esquerda) - self.getAltura(root.direita)
    # Busca da chave na árvore
  def search(self, root, value):
    if type(value) is list: #para recuperar uma lista de registros
      lista_indices = []
      for valor in value:
        lista_indices.append(self.search(root,valor))
      return lista_indices
    if type(value) is int: #para recuperar um único registro
      if root == None:
        return None
      if root.chave == value:
        return root.ind
      if value < root.chave:
        return self.search(root.esquerda, value)
      return self.search(root.direita, value)





