#Input --> Usar para coletar dados...

input('Qual o seu nome? ') # Ela não faz nada no código em si.  Apenas é exibida no terminal

'''
Você pode coletar dados da variável. Ex:
nome = input('Qual o seu nome?')
'''

nome = input('Qual o seu nome?')
numero_1 = input('Digite um número:')
numero_2 = input('Digite outro número')

# Aqui se ver a importÂncia da coerção dos dados. Tipo, vc pega um dados em str e vai precisar converter depois. Isso porque o input sempre recebe string, então caso queira trabalhar com números é mais complicado

print(f'A soma dos número é: {numero_1 + numero_2}') # 15 pois concatenou string

# Maneira correta de se aplicar isso

numero_1c = int(input('Digite um número:'))
numero_2c = int(input('Digite outro número'))

print(f'A soma dos número é: {numero_1c + numero_2c}') # 6, pois foi convertido o input

# Isso vai  funcionar, mas converter dessa forma é ruim... pois caso eu queira saber o que o usuário digitou antes que seja  convertido para inteiro e ele tenha digitado "A" que é uma 'str' não vai ser possível converter e se converter  vai dá erro. Logo seu programa vai de  F pois vai dar erro.

# 1° checar antes, depois converter

numero_4c = input('Digite um número:')
numero_3c = input('Digite outro número')

numero_check4 = int(numero_4c)
numero_check3 = int(numero_3c)




