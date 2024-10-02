# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados) # Desempacotando o dicionário fica assim
# p1 = pessoa(nome='João', idade=35)

# >>>>> Ou seja vai transformar o dict em objeto/instância

# p1.nome = 'EITA'
# print(p1.idade)

# >>> Editando pelo dicionário 
# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'EITA'
# del p1.__dict__['nome'] 

# print(p1.__dict__) --> onde fica armazenado os dados, tudo em dicionários

# print(vars(p1))
# print(p1.outra)
# print(p1.nome)
print(vars(p1)) # --> mostra os dict tbm
print(p1.nome)