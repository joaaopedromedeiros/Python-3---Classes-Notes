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

