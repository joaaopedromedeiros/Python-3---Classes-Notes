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


# Apagando uma chave com del
del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])


# print(pessoa.get('sobrenome'))

# Tenta obter, se n tiver NÃO EXISTE se tiver tenta mostrar

if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')