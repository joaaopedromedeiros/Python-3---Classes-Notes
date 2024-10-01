# areas

a = float(input("Digite um valor A: "))
b = float(input("Digite um valor B: "))
c = float(input("Digite um valor C: "))


# Alternativa A
print("Calculando área do triangulo com pontos A e C ")

area = ( a * c ) / 2
print(f'TRIANGULO: {area:.3f}')


# Alternativa B
print("Calculando a área de um circulo com raio com valor de C")

pi = 3.14159
r = c
area_circulo = pi *  (r ** 2)

print(f'CIRCULO: {area_circulo:.3f}')

# Alternativa C

# area trapézio: (B+b) × h / 2

print("Calculando a área do trapezio com altura A e B, com altura C")
area_trapezio = ( ( a + b) * c ) / 2
print(f'TRAPEZIO: {area_trapezio}')

# Alternativa D

print("Calculando a area de um quadrado de base B")
area_quadrado = b ** 2
print(f'QUADRADO: {area_quadrado:.3f}')

# Alternativa E

print("Calculando a área de um retângulo com base e altura, respectivamente, A e B ")

area_retangulo = a * b
print(f'A área do retangulo é: {area_retangulo:.3f}')




