# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

# Explicando o copy() abaixo: d2 = d1, como o dict é mutável então na verdade vc estaria atribuindo o valor diretamente sem fazer copia, como uma lista. Então vc usa o método copy()

d2 = d1.copy()

d2['c1'] = 1000
d2['l1'][1] = 999999
# d2['l1][indice] = 99999, equivale ao zero

print(d1)
print(d2)