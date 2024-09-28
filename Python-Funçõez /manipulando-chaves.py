# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

# Criando um dictionary dinamicamente

chave = 'nome'

# pessoa['nome'] = 'Luiz Otávio'
# Abaixo eu criei usando a variável
pessoa[chave] = 'Luiz Otávio'

# Aqui abaixo usei a forma normal
pessoa['sobrenome'] = 'Miranda'


print(pessoa[chave])

pessoa[chave] = 'Maria'


# Apagando del
del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')