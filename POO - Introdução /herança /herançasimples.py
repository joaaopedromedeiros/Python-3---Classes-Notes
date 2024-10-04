# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
class Pessoa:
    cpf = '1234'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('Classe PESSOA')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('EITA, nem saí da classe CLIENTE')
# Exibe primeiro pq executa primeiro, o method resolution order vem aqui primeiro de baixo pra cima
        print(self.nome, self.sobrenome, self.__class__.__name__)

# Herdou colocando (Pessoa)


class Aluno(Pessoa):
    cpf = 'cpf aluno'
    ...

# esse cpf aluno tem prioridade pois o resolution method é de baixo pra cima --> Method resolution order MRO


c1 = Cliente('Luiz', 'Otávio')
c1.falar_nome_classe()
a1 = Aluno('Maria', 'Helena')
a1.falar_nome_classe()
print(a1.cpf)
# help(Cliente)