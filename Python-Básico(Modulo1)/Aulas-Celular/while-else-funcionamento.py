""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')


# O else é excutado após todo o while ser executado. Mas, se o while tiver um break, o else não é executado.

#Não confunda else com elif ou else de do IF