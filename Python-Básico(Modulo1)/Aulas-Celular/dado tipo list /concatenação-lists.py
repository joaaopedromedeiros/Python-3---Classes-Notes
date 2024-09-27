"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b # adiciona uma a outra
lista_a.extend(lista_b)

# extende a lista a juntando com os itens da lista b. Se vc der print em uma variável com esse código não aparece nada, pois na verdade tudo de B foi para A, devido o extend ter extendido a lista_a em toda a B

print(lista_a)