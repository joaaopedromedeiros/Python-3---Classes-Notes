# 55

# pega x, dps coloca y e soma


validação = 0
numeros = [1,2,3,4,5,6,7,8,9,10]
soma = 0

while validação < 10:
    for x in numeros:
        soma = x + soma
        validação += 1
        
print(soma)