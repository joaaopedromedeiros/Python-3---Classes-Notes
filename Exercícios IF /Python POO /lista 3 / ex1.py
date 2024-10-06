# Lista 3 - POO
# Exercício 1

# h - altura
# b - base 
class Retangulo:
    def __init__(self, b, h):
        self.b = b
        self.h = h
        
    def setBase(self, b):
        self.b = b 
    def setAltura(self, h):
        self.h = h
        
    def getBase(self, b):
        return self.b 
        
    def getAltura(self, h):
        return self.h 
    
    def CalcArea(self):
        area = self.b * self.h
        return f'sua area é {area}'
        
    def CalcDiagonal(self):
        diagonal = ((self.b)**2 + (self.h**2))** 0.5
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




        
    
    
    


