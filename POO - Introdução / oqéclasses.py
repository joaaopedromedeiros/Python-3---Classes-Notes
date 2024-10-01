# Oq é classes?

# class - Classes são moldes para criar novos objetos

# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.

# Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações.

# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())

# print(isinstance(string, str))
# Checa se a string é um objeto (instância) da classe STR 

# A classe responsável por todo funcionamento da string é classe str


class Pessoa:
    ...

# Agora já tem uma classe, por mais que não tenha nada dentro. Posso gerar as coisas nesse objeto (instância) 


p1 = Pessoa('Luiz', 'Otávio')
p1.nome = 'Luiz'
p1.sobrenome = 'Otávio'

p2 = Pessoa('Maria', 'Joana')
p2.nome = 'Maria'
p2.sobrenome = 'Joana'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)