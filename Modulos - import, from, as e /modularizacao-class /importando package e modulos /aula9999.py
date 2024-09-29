import pasta_package.modulo
from pasta_package import modulo
from pasta_package.modulo import * # má prática 

# from pasta_package.modulo import soma

# print(*path, sep='\n')

print(soma(1, 2))
print(pasta_package.modulo.soma(1, 2))
print(modulo.soma(1, 2))

# com má prática 
print(variavel)
print(nova_variavel)