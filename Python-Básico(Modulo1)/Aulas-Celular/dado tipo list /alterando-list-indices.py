"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]

# lista[2] = 300
# del lista[2] --> não recomendado pois deleta indice e pd demorar pra processar se for uma lista enorme
# print(lista) --> atualizou com o 300
# print(lista[2]) --> pegou apenas o elemento do indice 2

lista.append(50) # adiciona na última posição da lista
lista.pop() # excluir o último da lista, no momento, que no caso é 50
lista.append(60) 
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor) 

# apenas visualizando até mesmo o valor excluido se colocado em uma variável