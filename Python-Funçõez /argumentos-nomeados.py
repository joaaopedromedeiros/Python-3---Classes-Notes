"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3)
soma(1, y=2, z=5) # nesse caso não vai depender da ordem respectiva dos parâmetros, pois estou definindo os valores dos argumentos (de cada parâmetro) enquanto chamo a função 


# OBS: Todos argumentos precisam ser nomeados caso vc faça a nomeaçâo de pelo menos 1 anterior. Os próximos vão precisar serem também!

print(1, 2, 3, sep='-')