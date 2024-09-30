# Lista 2 | Tipos básicos de Python 

# Exercício 1
#entrada = input("Qual o seu nome?")


#print(f"Seja bem vindo ao python,  {entrada}")
# funcionando (acima), só tirar os '#'

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Exercicio 2

# Utilize o método split(), pois divide as palavras baseado no que vc passa entre (), que em vazio  é o espaço por padrão.

# entrada_print = input("Digite o seu nome completo: ")

# primeiro_nome = entrada_print.split(" ")

# Ele deixa tudo em uma lista e vc chama o indice 0



# print(f'Seja bem vindo ao Python {primeiro_nome[0]}')

# Funcionando (acima )

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Exercicio 3 

# b1 = peso 2
# b2 = peso 3

# nota_1 = input("Digite a sua nota do primeiro bimestre: ")
# nota_2 = input("Digite a nota do segundo bimestre: ")


# print("Sua nota média parcial está sendo calculada....")
# print()

# converter_1 = int(nota_1)
# converter_2 = int(nota_2)


# Media ponderada : 
# (B1 × 2) + (b2 × 3) / B1+B2

# def mediaparcial(b1,b2):

    #return  ( (b1 * 2)+ (b2 * 3) ) / 5

# c = mediaparcial(converter_1,converter_2)
# print(c)


# funcionando (acima )

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#exercicio 4

# Calcular área, perímetro e diagonal de um retângulo, dados sua base e sua altura. Considerar que os valores 

# podem ser números reais. Mostrar o resultado com duas casas decimais.

entrada_medidas = input("Digite a área e a base do retangulo, respectivamente: ")

separar_dados = entrada_medidas.split(" ")

base = separar_dados[0]
altura = separar_dados[1]

try:
    converter_base = int(base)
    converter_altura = int(altura)
except:
    print("Algo deu errado...")


print(base)
print(altura)

print("Vamos calcular a área, perimetro e valor da diagonal de seu retângulo automaticamente")

area = converter_base * converter_altura 
perimetro = (converter_base * 2) + (converter_altura *2)

# Calculando diagonal a² = b² + c²

b2_c2 =  converter_base ** 2 + converter_altura ** 2

a2 = b2_c2 ** 0.5

print(area)
print(perimetro)
print(f'{a2:.2f}')

# funcionando (acima)


