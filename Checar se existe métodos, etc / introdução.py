# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'strip' # poderia ser  'upper'

if hasattr(string, metodo):
    print('Existe strip')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)