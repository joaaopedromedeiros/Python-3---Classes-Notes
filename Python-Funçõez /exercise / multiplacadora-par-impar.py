def multiplica(*args):
    # total = 0 --> total 0 * any number = 0
    total = 1
    for numero in args:
        total *= numero
    return total
    
    
mult = multiplica(1,2)
print(mult)


def par_ou_impar(number):
    if number % 2 == 0:
        return f'{number} é par'
    if number % 2 != 0:
        return f'{number} é impar'

check = par_ou_impar(10)
print(check)


# =============================

# Misturando as duas funções 

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    
    if total % 2 == 0:
        return f'O resultado da multiplicação é {total}, e ele  é par'
    if total % 2 != 0:
        return f'O resultado da multiplicação é {total}, e ele  é impar'
    
    
mult = multiplica(1,5)
print(mult)



