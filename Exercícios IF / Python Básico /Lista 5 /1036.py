# Equação do segundo grau automatizada

# ax² + bx + c
# ◇ = -b + 4ac

# Equação do segundo grau automatizada

# ax² + bx + c
#◇ --> raiz
# baskara: x = (-b +/ ◇ Delta)/2
# Delta = b²-4ac


a = float(input("Digite um numero para A"))
b = float(input("Digite um numero para B"))
c = float(input("Digite um numero para C"))

a_vezes_c = a * c
delta = (b ** 2) -4 * a_vezes_c

if (a != 0) or (delta < 0):
    x1 = ( -(b) + (delta ** 0.5) ) / (2 * a)
    x2 = ( -(b) - (delta ** 0.5) ) / (2 * a)
    # meu erro foi elevar delta ao quadrado, com ** 2 e não ter elevado a raiz ( ** 0.5)
    print(f'{x1:.5f}')
    print(f'{x2:.5f}')
else:
    print("Impossível calcular devido o A ou delta calculado na situação ser menor que zero")
    










