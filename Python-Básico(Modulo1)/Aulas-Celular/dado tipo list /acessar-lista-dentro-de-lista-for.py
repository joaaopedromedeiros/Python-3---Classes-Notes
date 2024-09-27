"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# buscando dados de cada lista dentro delas mesma. Buscando a sala ( 3 salas (0,2) ) e alunos dentro da sala

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])

# Busca a sala, busca os alunos em cada sala 

for SALA in salas:
    print(f'A sala é {SALA}')
    for aluno in SALA:
        print(aluno)