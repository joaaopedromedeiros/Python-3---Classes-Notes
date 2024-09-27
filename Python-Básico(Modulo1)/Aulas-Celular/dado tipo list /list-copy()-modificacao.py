"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""




lista_a = ['Luiz', 'Maria', 1, True, 1.2]

lista_b = lista_a 

# Aqui modifica nas duas pois é mutável, os dados aponta para a lista original A, são os mesmos. se der print(lista_b), vai aparecer modificado.

# lista_b = lista_a.copy()

# Se fosse nessa situação acima, vc copiou a lista original então se modificar algo na primeira nada muda no print(lista_b), pois é uma copia.

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)

