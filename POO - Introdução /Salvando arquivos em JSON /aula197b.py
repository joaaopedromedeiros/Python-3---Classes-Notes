# Recuperando/utilizando dados/arquivos


import json # precisa 

from aula127_a import CAMINHO_ARQUIVO, Pessoa, fazer_dump # precisa 


# fazer_dump()

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])
    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)

# with open(Caminho que vc definiu, 'r'), as variável definida:
 algo = json.load(variável que vc definiu) 


# r --> read 