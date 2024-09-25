# Segunda aula de formatação de f strings. Substituições

# s - string
# d, i - int

# f - float
# x e X - hexadeciimal (ABCDEF#12345678)
# (Caractere)(><^)(quantidade)
# > - Esquerda
# < - Direita
# ^ - Centro
# Sinal - + ou -
#Ex: 0>100,.1f
# Conversion flags - !r !s "a"

variavel = "ABC"
print(f"{variavel}")
print(f"{variavel: >10} ") #  Preencheu 10 caracteres para  esquerda no terminal

print(f"{variavel: $<10} ") 
print(f"{variavel: ^10} ") 
print(f'{1000.0312301230128309283:0>+10,.1f}')

# esse  + indica  que  o python mosra  se o vlor forr positivo



