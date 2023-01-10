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

from AVLTree import *
import time

def cria_arvore():
    f = open('bd_avl.txt')
    st = time.perf_counter()
    avl = AVLTree()
    root = None
    for i,linha in enumerate(f.readlines()):
      indx = linha.split(';')
      chave_primaria = int(indx[0])
      root = avl.insert_node(root, chave_primaria, i+1)
    print("Tempo gasto para criar a árvore AVL: ",\
          time.perf_counter() - st, " segundos.")
    f.close()
    return avl, root

def brute_force(chave):
    f = open('bd_avl.txt')
    st = time.perf_counter()
    for i,linha in enumerate(f.readlines()):
      indx = linha.split(';')
      chave_primaria = int(indx[0])
      if chave == chave_primaria:
        f.close()
        print("Tempo gasto para encontrar a chave na força bruta: ",\
          time.perf_counter() - st, " segundos.")
        return i+1
    print("Tempo gasto para encontrar a chave na força bruta: ",\
          time.perf_counter() - st, " segundos.")
    f.close()
    return None

def busca_AVL(avl, root, chave):
    st = time.perf_counter()
    res = avl.search(root,chave)
    print("Tempo gasto para encontrar a chave na árvore AVL: ",\
          time.perf_counter() - st, " segundos.")
    return res

avl, root = cria_arvore()

ind_bf = brute_force(165974181)

ind_avl = busca_AVL(avl, root, 165974181)

print(f"""O índice retornado pela força bruta foi {ind_bf}, e pela
busca na árvore AVL foi {ind_avl}.""")



