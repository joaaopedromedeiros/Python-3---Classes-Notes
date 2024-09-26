"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

contador = 0
while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)
    if contador == 40:
        break

print('Acabou')

# Ao chegar na condição do continue executa tudo que ta no bloco de código dele, mas só ele é executado e acaba não  mostrando o print(contador) nele