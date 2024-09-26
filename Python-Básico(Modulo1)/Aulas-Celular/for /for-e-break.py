for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')

# Ou seja o continue é igual no while, o break também, else 

# continue: volta pro início do bloco de código, pula o que vc falar pra pular  e volta
# break: para todo o código e não fala o else, pula pra fora de todo o bloco de código
# else: é executado após todo while ser finalizado/executado

# O while vc não sabe quantas repetições o usuário vai realizar. No for vc sabe... e define