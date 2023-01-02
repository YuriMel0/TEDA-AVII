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

class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita
        self.altura = 1.0

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,self.chave,self.direita and self.direita.chave)

class AVLTree(object):

  def insert_node(self, root, key):
        # Find the correct location and insert the node
        if not root:
            return NodoArvore(key)
        elif key < root.chave:
            root.esquerda = self.insert_node(root.esquerda, key)
        else:
            root.direita = self.insert_node(root.direita, key)

        root.altura= 1 + max(self.getHeight(root.esquerda),
                              self.getHeight(root.direita))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key < root.esqueda.chave:
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

    # Function to perform left rotation
  def leftRotate(self, z):
        y = z.direita
        T2 = y.esquerda
        y.esquerda = z
        z.direita = T2
        z.altura = 1 + max(self.getHeight(z.esquerda),
                           self.getHeight(z.direita))
        y.altura = 1 + max(self.getHeight(y.esquerda),
                           self.getHeight(y.direita))
        return y

    # Function to perform right rotation
  def rightRotate(self, z):
        y = z.esquerda
        T3 = y.direita
        y.direita = z
        z.esquerda = T3
        z.altura = 1 + max(self.getHeight(z.esquerda),
                           self.getHeight(z.direita))
        y.altura = 1 + max(self.getHeight(y.esquerda),
                           self.getHeight(y.direita))
        return y

    # Get the height of the node
  def getHeight(self, root):
        if not root:
            return 0
        return root.altura

    # Get balance factore of the node
  def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.esquerda) - self.getHeight(root.direita)