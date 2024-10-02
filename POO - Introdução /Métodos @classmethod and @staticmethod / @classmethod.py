# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # @classmethod # --> Faz ser possível funcionar o método mesmo sem ser associado a uma instância/objeto. Analise que tudo agora é cls e não self, pois agora é executado mesmo sem ter uma instância como p1.algo

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

# Apenas por por Pessoa.metodo_de_classe() já funciona mesmo sem passar instâncias/objetospois a própria classe substitui, devido o @classmethod...

    @classmethod
    def criar_com_50_anos(cls, nome): 
# cls = classe, nome --> define e o 50 segue a ordem da classe como idade, por isso fala p2.idade e aparece 50
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)


p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa('Anônima', 23)
p4 = Pessoa.criar_sem_nome(25)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)

# print(Pessoa.ano) --> cls, sem instância/objeto
# Pessoa.metodo_de_classe() --> cls, sem instância/objeto