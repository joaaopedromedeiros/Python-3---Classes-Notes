import importlib

import aula98_m

print(aula98_m.variavel)

for i in range(10):
    importlib.reload(aula98_m) # recarrega
    print(i)
print('Fim')


print(123)
variavel = 'Luiz 1'