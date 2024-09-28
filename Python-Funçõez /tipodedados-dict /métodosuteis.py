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
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 900,
}

pessoa.setdefault('idade', 0) # define por padrão  que existe ('nome', valor)
 
print(pessoa['idade'])

# print(len(pessoa)) --> ver quantidade de chaves que tem

# print(pessoa.keys()) --> ver todas as chaves

# print(list(pessoa.keys())) --> tosas as chaves
# print(list(pessoa.values())) --> todos os valores de cada chave
# print(list(pessoa.items())) --> chaves e os valores

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)