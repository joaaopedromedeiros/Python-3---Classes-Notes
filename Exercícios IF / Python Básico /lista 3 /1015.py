#distância entre dois pontos

# digite as distâncias de um ponto cartesiano 
# x1 & y1

# digite as distâncias de outro pontos cartesianos
# x2 & y2


# ache a distância entre eles ( Repare que isso vai gerar um triangulo retangulo, logo apenas utilizo a formula de pitagoras ) 


# My

valores_1 = input("Defina dois pontos x1 e y1, respectivamente: ")

valores_2 = input("Defina mais dois pontos x2 e y2, respectivamente: ")

# distancia raiz disso: 
#(x2-x1)² + (y²-y¹)²

print("dados 1")
split_1 = valores_1.split(" ")
print(split_1)



# x1 = split_1[0]
# y1 = split_1[1]

x1 = float(split_1[0])
y1 = float(split_1[1])

# devido split gerar uma lista com string
# Convertendo os dados com float


print("dados 2")
split_2 = valores_2.split(" ")
print(split_2)

# x2 = split_2[0]
# y2 = split_2[1]

x2 = float(split_2[0])
y2 = float(split_2[1])


exponencial = (x1 - x2)**2 + (y2 - y1)**2
raiz = exponencial ** 0.5

print(f'{raiz:.4f}')









