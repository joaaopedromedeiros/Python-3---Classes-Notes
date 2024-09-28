"""
Retorno de valores das funções (return)
"""


# def soma(x, y): --> x,y = ingredientes
# escopo = ações com esse ingrediente 
#    return x + y -->  O que vc vai fornecer do que foi feito com os ingredientes para o resto do código

# significa que sua função vai te retornar valores para utilizar em variaveis, etc e executar cálculo, etc. Sem o return a função seria NoneType e não conseguia reaproveitar os valores pra usar eles no resto do código.


def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y
    # print("...") --> depois de return não funciona mais nada. A função vai retornar tudo que já foi executado pro código.


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