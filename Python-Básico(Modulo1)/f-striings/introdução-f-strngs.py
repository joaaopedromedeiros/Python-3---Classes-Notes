# Introdução a f-strings (Uma das formas de formação de strings)

# Quero por esse conteúdo da aula passada em apenas um lugar só sem ter quue por em print.

# Original

nome = 'Luiz Otavio'
altura = 1.80
peso = 95
imc = (peso/ (altura ** 2) )

print( "Estudante", nome,"tem de Altura", altura, "e pesa", peso, " com IMC de", imc)

# IMC = 29.3209876...

# Apenas na variável (f-strinngs)
# Abilito usar funções dentro da string apenas colocando o f

linha_1 = f'{nome} tem de altura {altura} e pesa {peso} com IMC DE {imc}'
print(linha_1)

print(" Agora...formatando a quantidade de casas casas decimais")

linha_1 = f'{nome} tem de altura {altura:.2f} e pesa {peso} com IMC DE {imc}'
print(linha_1)

print(" Agora...formatando a quantidade de casas casas decimais emm virgula")

linha_1 = f'{nome} tem de altura {altura:,.2f} e pesa {peso} com IMC DE {imc:.2f}'
print(linha_1)
