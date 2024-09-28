"""
Closure e funções que retornam outras funções
"""


# def criar_saudacao(saudacao,nome):
#    def saudar():
#        return f'{saudacao}, {nome}
#     return saudar --> devido aqui não ter (), vc coloca no momento do print 

#

#s1 = criar_saudacao(bom dia, Luiz)
# print( s1() )




def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')



# estrutura de repetição 

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))