"""
Iterando strings com while
"""
#       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321


nome = 'Maria Helena'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)

# My Exercise
nome = "João Pedro"

novo_nome = ""
indice = 0


# Repetição de nome estilizado 

while indice < len(nome):
    pegar_letra = nome[indice] # com o nome e o indice consigo a letra

    novo_nome += f'*{pegar_letra}' # esse += fala que é pra concatenar na string "novo_nome" o resultado do "pegar_letra"

    indice += 1 # faz que so pare de realizar isso ao ter a mesma quantidade de caracteres no indice do nome original 
    
print(novo_nome)