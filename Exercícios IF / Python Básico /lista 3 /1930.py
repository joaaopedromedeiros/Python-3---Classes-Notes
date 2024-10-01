# tomadas elétricas

# maximo de tomadas juntas 

# Quantidade de tomadas ocupadas  está entre 2 menor ou igual Ti menor ou igual a 6, logo vai ser 4

# map(função, argumentos (tuplas, lista, iteráveis))

input("Digite 4 valores com a quantidade de strips ")

T1, T2, T3, T4 = map(int, input().strip().split())

# Ta transformando o input().strip().split() em INT diretamente 

# Calculate the maximum number of devices that can be connected 
max_devices = T1 + (T2 - 1) + (T3 - 1) + (T4 - 1)

# Print the result
print(max_devices)



# Entendi POUCA COISA

