# Funções decoradoras e decoradores com classes
# Criando uma classe decoradora

def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr

# criando acima as funcionalidades da syntaxes sugar ( acima é aquele repr de ver valor, dá pra fz com str ) 

def adiciona_repr(cls):
    cls.__repr__ = meu_repr 
# método cls.__repr__ = a outra função criada 
# como se fosse atualizada 
    return cls


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome
@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome
brasil = Time('Brasil')
portugal = Time('Portugal')
terra = Planeta('Terra')
marte = Planeta('Marte')
print(brasil)
print(portugal)
print(terra)
print(marte)


# OBSERVAÇÕES 

# >> O CLS como parâmetro faz o a gente ter acesso as classes que o @... ficar em cima.
# Assim, a gente consegue atribuir as coisas do
# syntaxes sugar a classe de baixo normal. 
