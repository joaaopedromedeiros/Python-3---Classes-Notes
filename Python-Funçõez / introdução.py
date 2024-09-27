"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

#def FunçãoName(parâmetros):
 #algo vai ser executado




# esse parametros ( que é como se fossem uma variáveis criadas) vão receber valores em algum momento e por isso no scopo são argumentos,  e vc precisa dar os seus valores de cada parâmetro se n dá erro ao chamar ele. Se tem a,b,c de argumento, ao chamar na função é --> funcao(valor a, valor b, valor c)


# exemplo disso tudo
# def imprimir(a,b,c):
#  print("sla")


# imprimir(1,2,3) 

# O que é o que? 
# a --> parâmetro, e
# 1 --> o argumento do parâmetros >>a<<



# Exemplo real

def imprimir(a, b, c):
    print(a, b, c)


imprimir(1, 2, 3)
imprimir(4, 5, 6)

# os argumentos substituindo as variáveis (parâmetros) 


 


# def Print(a, b, c):
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')




def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')


saudacao('Luiz Otávio')
saudacao('Maria')
saudacao('Helena')
saudacao()