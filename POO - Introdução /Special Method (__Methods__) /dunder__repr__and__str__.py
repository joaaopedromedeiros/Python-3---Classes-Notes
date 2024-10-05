# Python Dunder Methods __repr__ e __str__
# Ambos métodos servem para mostrar o valor
# em string, mas há diferenças.


# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
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
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

# __str__ = Geralmente usado para mostrar ao
# usuário, os valores dos argumentos dos objetos que 
# usam a classe

    def __str__(self):
        return f'({self.x}, {self.y})'

# __repr__ = Usado para mostrar aos
# desenvolvedores como você deseja mostrar os 
# valores

    def __repr__(self):
        # class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'

# p1 = um objeto, Classe(Argumento1,Argumento2) 
p1 = Ponto(1, 2)
p2 = Ponto(978, 876)

print(p1)
print(repr(p2))

print(f'{p2!r}') 
# esse !r é apenas para forçar que mostre a str +
# __repr__. Sem isso só mostra o valor da str. 



# OBSERVAÇÕES 

# >> __repr__
# Não se assuste, é simples! 
# def __repr__(self):
#        class_name = type(self).__name__
#        return f'{class_name}(x={self.x!r}, 
# y={self.y!r}, z={self.z!r})'

# class_name = type(self).__name --> padrão
# esse __name__ retorna nome da classe 
# o return só chama o nome da classe & exibe 
# o self.x, self.y e self.z como se fosse apenas
# o STR. Mas, para chamar o __repr__ sem precisar
# forçar com o print, ele também colocou !r neles.