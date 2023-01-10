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

import random
f = open('bd_avl.txt', 'w')

n = 1000000
step = 420

for _ in range(n):
  #ident;idade;sexo
  ident = 123456789 + step
  idade = random.randint(18,60)
  aux = random.randint(0,1)
  if aux == 0:
    sexo = 'F'
  else:
    sexo = 'M'
  linha = f'{ident};{idade};{sexo}\n'
  step += 69
  f.write(linha)

f.close()
