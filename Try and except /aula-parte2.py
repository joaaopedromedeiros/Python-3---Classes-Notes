# (Parte 2) try e except para tratar exceções
# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__) 

# pega a class do erro >>.__class__<< ( pois eles são classes ) e depois o nome .__nome__ da classe

except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')