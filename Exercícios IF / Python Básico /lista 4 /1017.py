# gasto de gasolina


informe = input("Quanto tempo vc gastou na viajem, em horas, e qual a media de velocidade por km/h, respectivamente? ")



dados = informe.split(" ")
print(dados)

tempo = float(dados[0]) # tá em hora
km_h = float(dados[1]) # vm por hora (Ex: 10km/h, em 10h --> 100km)

# 1°) Calcula a distância (em km)
# Então:

distancia = tempo * km_h # =  tantos km


# 2°) Mostra quantos litros precisou 
# Então:

# 12km      --> 1l
# tantos km --> y litros 

# tantos km = tempo * km_h
# Daí:
# 12y = tempo * km_h
# y = tempo * km_h / 12 


# y -->  litros 

litros = (tempo * km_h) / 12

print(litros)

