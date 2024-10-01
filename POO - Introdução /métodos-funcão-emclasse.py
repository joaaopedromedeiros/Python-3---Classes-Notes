# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamente no código
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')
# todo método recebe self se está se referindo a instância (objetos)

string = 'Luiz'
print(string.upper())

fusca = Carro('Fusca') # param 1 (nome) = Fusca 
print(fusca.nome)
fusca.acelerar() 

# Não passo nada nesse parâmetro pois já tem o self

# Self = nome do objeto (instância), é o argumento --> fusca... dps a função faz o trabalho dela

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()