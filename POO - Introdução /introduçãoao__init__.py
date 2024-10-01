# Introdução ao método __init__ (inicializador de atributos)

# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

# >>>>>>>> Classificações
# self: Se referência ao objeto (instância) que esta sendo criado
# __init__: Ele inicializa os atributos da classe 
# nome:  Atributo
# sobrenome:  Atributo 


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

# Observações ao definir os parâmetros:
# 1°) Usa a função def __init__(Parâmetros): ..
# 2°) Precisa ser o primeiro param o self, obrigatoriamente, e dps vc pd passar o resto.

>>>>>
# O que acontece com esse self? Assim que vc a classe dentro de uma instância (objeto), ex:  "p1",  o python já chama ele automaticamente. 

# Como o self assume o valor de "p1" é como se tivesse fazendo p1.nome = algo, mas fica self.nome = algo 

>>>>>>>>>

# 3°) Cria os atributos com self.parametro = 

p1 = Pessoa('Luiz', 'Otávio') # argumentos nome,sobrenome  

# p1.nome = 'Luiz' --> p1 vira self 
# p1.sobrenome = 'Otávio'

p2 = Pessoa('Maria', 'Joana')

# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)