"""
Retorno de valores das funções (return)
"""


def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y


# variavel = soma(1, 2)
# variavel = int('1')
soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11, 55))


#Anotações

# Existem dois tipos de funções:
# 1. Apenas executam ações e retorna None, como o print
# 2. E outras que são específicas para retornar valores 