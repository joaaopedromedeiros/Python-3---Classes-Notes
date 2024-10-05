# Exemplo de uso de dunder methods (métodos mágicos)

# Operações com esses objetos 
# Ex. Objeto : C1 = algo, C1 é um objeto

# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})'


# Criando o método para usar nos objetos de mesma classe 
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other


if __name__ == '__main__':
    p1 = Ponto(4, 2)  # 6
    p2 = Ponto(6, 4)  # 10
    p3 = p1 + p2 # self + other 

    print(p3)
    print('P1 é maior que p2', p1 > p2)
    print('P2 é maior que p1', p2 > p1)



# OBSERVAÇÕES 
# >> other.x? other.y?
# Eu ativo o _add_, ou outro método, 
# para usar com  objetos que possuem a mesma
# classe! Então esse other.x é o do outro objeto
# da mesma classe que estiver somando. 


# >> sobre a operação p1 + p2
# Eu poderia retornar qualquer coisa ao realizar
# essa operação entre objetos! 
# Abaixo: 
# def __add__(self, other):
#        novo_x = self.x + other.x
#        novo_y = self.y + other.y
#        return Ponto(novo_x, novo_y)
# return = poderia ser qualquer coisa! Mas...
# Eu criei uma lógica no escopo da def utilizando os 
# atributos self.x e self.y e retornei oq eu criei
