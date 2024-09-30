#média ponderada



entrada = int(input("Digite um numero: "))
entrada_2 = int(input("Digite outro numero: "))


# pesos
# 3.5 - entrada
# 7.5 - entrada 2
media_ponderada = ( (entrada * 3.5) + (entrada_2 * 3.5) ) / 11

print(f'Média: {media_ponderada:.5f}')

