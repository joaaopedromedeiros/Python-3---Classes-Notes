"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""

frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',') # eu defini ondr quero cortar, na virgula 


lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip()) # strip apenas corta tirando os espaços

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)

# frases_unidas = 'como unir'.join(oq vou unir)
print(frases_unidas)