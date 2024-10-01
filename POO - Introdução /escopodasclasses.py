# Escopo da classe e de métodos da classe (namespace --> escopo ) 

# Escopo da classe, escopo de cada função interna
# Variáveis pertencem a cada escopo.

class Animal:
    # nome = 'Leão'

    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel) # Funciona pois ta no escopo, fora ou qlq outro lugar aparece que é outrange.  Ele inicia logo com o init, se chamar essa classe

    def comendo(self, alimento):
        return f'{self.nome} está comando {alimento}'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs) 
# retornando a outra função apenas


leao = Animal(nome='Leão')
print(leao.nome)

# >>>>>>>>>>>>>>>
# print(leao.comendo('maça')

# Nesse print eu não passo Leão como argumento pois a instância leao já tem como atributo definido, eu defini no leao = ... , o nome. Então só passa o atributo da comida pois o self é definido pelo self.nome já atribuido.
# >>>>>>>>>>>>>>>>

print(leao.executar('maçã'))

