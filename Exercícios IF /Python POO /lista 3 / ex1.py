# Lista 3 - POO
# Exercício 1

# h - altura
# b - base 
class Retangulo:
    def __init__(self, b, h):
        self.__b = b
        self.__h = h
        
    def setBase(self, b):
        self.__b = b 
    def setAltura(self, h):
        self.__h = h
        
    def getBase(self, b):
        return self.__b 
        
    def getAltura(self, h):
        return self.__h 
    
    def CalcArea(self):
        area = self.__b * self.__h
        return f'sua area é {area}'
        
    def CalcDiagonal(self):
        diagonal = ((self.__b)**2 + (self.__h**2))** 0.5
        return f'sua diagonal é {diagonal}'
    
    def __str__(self):
        return f'A base do seu retângulo é {self.b} e sua base mede {self.h}'
    
# não entendi a parte de baixo, estudar staticmethod
class UI:
    @staticmethod
    def main():
        b = float(input('Digite a base do retângulo: '))
        h = float(input('Digite a altura do retângulo: '))

        r = Retangulo(b, h)

        print(r)
        print(r.CalcArea())
        print(r.CalcDiagonal())
    

UI.main()



# falta por os IF caso coloque 0 e levanta error value, pois não pd por 0 pq multiplica e zera tudo



        
    
    
    


