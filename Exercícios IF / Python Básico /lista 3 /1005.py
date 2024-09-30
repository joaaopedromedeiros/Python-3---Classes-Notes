#média ponderada



entrada = float(input("Digite um numero: "))
entrada_2 = float(input("Digite outro numero: "))


# pesos
# 3.5 - entrada
# 7.5 - entrada 2
media_ponderada = ( (entrada * 3.5) + (entrada_2 * 7.5) ) / 11

print(f'Média: {media_ponderada:.5f}')