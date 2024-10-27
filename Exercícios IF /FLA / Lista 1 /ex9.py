# valor = 4,85 soma fixa
# 3 por km (bandeira 1)
# 4,18 por km  (bandeira 2)


bandeira = int(input("Digite a bandeira do taxi: "))
distancia = float(input("Digite a distância percorrida em quilometro: "))

if bandeira == 1:
    custo_1 = 4.85 + (distancia * 3)
    print(f'O valor total da sua viagem é: {custo_1}')
elif bandeira ==2:
    custo_2 = 4.85 + (distancia * 4.18)
    print(f'O valor total da sua viagem é: {custo_2}')
    
