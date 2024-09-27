"""
Tipo tupla - Uma lista imutável
"""
nomes = ('Maria', 'Helena', 'Luiz')
# nomes = tuple(nomes)
# nomes = list(nomes)
print(nomes[-1])
print(nomes)

# vc só não precisa por o [], de array/lista e cria uma tupla de 3 dados ou mais... ( é mais rápido até que a lista). Mas como toda string, é imutável

# É uma string, mas chama de tuple o dado nesse formato de 3 ou mais strings como está acima. Se vc tentar mudar o dado, vai dar um erro "Tuple dont support item assignment "