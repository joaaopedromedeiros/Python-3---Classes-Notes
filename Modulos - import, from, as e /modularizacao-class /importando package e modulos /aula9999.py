import aula99_package.modulo
from aula99_package import modulo
from aula99_package.modulo import * # má prática 

# from aula99_package.modulo import soma_do_modulo

# print(*path, sep='\n')

print(soma(1, 2))
print(aula99_package.modulo.soma(1, 2))
print(modulo.soma(1, 2))

# com má prática 
print(variavel)
print(nova_variavel)