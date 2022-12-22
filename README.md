![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
## Avaliação II - Árvores AVL com índices de arquivos grandes

### Descrição de implementação da AVL:

Desenvolver um módulo, em C++ ou Python, que implementa parcialmente uma árvore AVL e utilizá-lo na resolução do problema descrito abaixo. A árvore deve ser projetada como uma classe OO e deve apresentar os seguintes métodos na sua interface:

1. Criação da árvore

2. Inserção de dado na árvore por chave k

3. Consulta por chave k. A resposta aqui é um objeto contendo o dado associado à chave k, ou o valor NULO, caso a chave k não esteja na árvore

4. Atualização de dado por chave k

### Situação Problema:

Desenvolva um procedimento de teste do “índice primário” que realiza, no mínimo, a seguintes operações:

1. Construção do índice primário a partir do arquivo dado: percorrer toda a extensão do arquivo, registro a registro, obtendo as suas chaves primárias e as insira na Árvore AVL, juntamente com o “ponteiro” (posição, ou número da linha) do registro no arquivo.

2. Utilizar o índice primário para realizar a recuperação de um registro dado a sua chave primária. Considere o caso da chave de busca fornecida não estar no índice, ou seja, não existe registro no arquivo com aquele valor de chave primária.

3. Dado um intervalo de chaves, recupere todos os registros cujas chaves primárias pertencem ao intervalo dado (nesse caso o retorno é uma lista de registros).


