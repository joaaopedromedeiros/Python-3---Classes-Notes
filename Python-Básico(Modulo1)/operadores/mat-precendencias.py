# Ordem de prioridade das operaçções (igual na matemática)
# Coisas sendo executadas antes das outras

#1. (n + n)
#2. ** (exponenciação)
#3. * (mulltiplicação) / (divisçao) // (divisão truncada) % (modulo)
#4. + (adição) - (subtração) 

# Esquerda para direita, de cima para baixo (leitura do interpretador lê)

conta_1 = 1 + 1 ** 5 + 5 # 7
print(conta_1)

# Por que?
# 1 + (1 elevado a 5 = 1) + 5 = 1 + 1 + 5






