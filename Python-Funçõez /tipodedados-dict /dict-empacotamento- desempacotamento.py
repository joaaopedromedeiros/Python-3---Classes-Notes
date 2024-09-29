⁸
# Empacotamento e desempacotamento de dicionários

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}


# >>Desempacotando no manual<<
# (a1, a2), (b1, b2) = pessoa.items() --> desempacotamento (Nome, Aline), (sobrenome, Souza) 

# print(a1, a2)
# print(b1, b2)

# >>Desempacotando com for in<<
# for chave, valor in pessoa.items():
#     print(chave, valor)


dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}


pessoas_completa = {**pessoa, **dados_pessoa, 'nome': 1}
# print(pessoas_completa)

# **pessoa --> extrair os dados de pessoa, mesma coisa con **dados_pessoas. Mas ainda possi add algo

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


# mostro_argumentos_nomeados(1,2,3, nome='Joana', qlq=123)

# posso pasaar argumentos nomeados e não nomeado, kwargs com "**" no parâmetro, lembre-se

# mostro_argumentos_nomeados(**pessoas_completa)


configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)