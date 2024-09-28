Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add('Luiz')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4)) 

# Voce precisa por em tupla para enviar um string!!! 

# s1.clear() --> limpa totalmentr 

s1.discard('Olá mundo') --> vc precisa digitar o valor
s1.discard('Luiz')
print(s1)

# Operadores úteis:
# união | união (union) - Une