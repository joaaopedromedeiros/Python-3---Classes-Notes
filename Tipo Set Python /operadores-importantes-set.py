# s1.clear()
s1.discard('Olá mundo')
s1.discard('Luiz')
print(s1)
# print(s1)

# Operadores úteis:

# Igual matemática 

# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos


s1 = {1, 2, 3}
s2 = {2, 3, 4}

# Operações 

s3 = s1 | s2 # união 
s3 = s1 & s2 # Intercessão 
s3 = s2 - s1 # Diferença 
s3 = s1 ^ s2 # Itens que não estão em ambos
print(s3)