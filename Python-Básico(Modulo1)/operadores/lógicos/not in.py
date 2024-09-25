# Operadores in and not in

# In - estar  entre
# In not - Não estar entre
# Strings são iteráveis --> Vc pode navegar item por item, índices

#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1 --> começo do negativo

nome = "otavio"

#print(nome[2])
#print(nome[-4])

print('á' in nome) # ele checa se 'a' está na variável nome (True or False)
print('vio' in nome)

print('10' not in nome) # checa se '10' >>não esta<< na variável nome.

# Exempplo bobo de aplicação

nome = input("Digite o seu nome: ")
encontrar = input("O que vc deseja encotrar dentro do nome? ")

if encontrar in nome:
  print("f'{encontrar} está em {nome}")
else:
  print("O {enontrar}  não se encontra em nome")
  


