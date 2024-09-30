# Variáveis livres + nonlocal (locals, globals)
# print(globals())
# def fora(x):
#     a = x --> variável livre 

#     def dentro():
#         # print(locals()) --> ver quais variáveis são locais 

#         return a
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())


def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final 

# --> sem isso o valor_final só pertence ao escopo da def concatenar, com isso o python consegue buscar lá.
 
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')

print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)


# Por que esse print funciona e concatena? 

# c = concatenar('a'), então ao chamar C, o resultado dessa função dentro dele  é o return que é = a função interna, então passa pela interna antes pra dps finalizar e sair o resultado.

# Quando passa pela função interna, o argumento >>a<< recebido pela no parâmetro da concatenar é adicionado com o outro argumento passado para "valor_a_concatenar" pois na função interna tem aquele codigo dizendo que adiciona ao valor final e dps  retorna o valor final e assim finaliza a interna, e dps a função concatenar retorna o resultado