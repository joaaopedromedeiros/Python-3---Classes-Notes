# Lista 10 - POO (Execeções)
# Ex1 

class Retangulo:
    def __init__(self, base, altura):
        if base <= 0: raise ValueError("A base deve der maior que zero")
        if altura <= 0: raise ValueError("A altura deve ser maior que zero")
        self._b = base 
        self._h = altura 
    
    def setBase(self, base):
            self._b = base

            
    def setAltura(self, altura):
            self._h = altura
            
    
    def getBase(self):
        return self_.b
    def getAltura(self):
        return self._h 
    
    def __str__(self):
        return f'A base do triangulo é {self._b} e altura {self._h}'
        
    def CalcArea(self):
        area = self._b * self._h
        return print(f'A área do seu retângulo é {area}')
        

class UI:
    @staticmethod
    def Main():
        base = int(input("Qual o valor da base do seu retângulo? "))
        altura = int(input("Qual o valor da altura do seu retângulo? "))
        retangulo = Retangulo(base, altura)
        

        print(retangulo)
        retangulo.CalcArea()
        
    
UI.Main() # Classe + método retorna o valor do método = toda função que coloquei



# Mesmo código mas com try catch

# Lista 10 - POO (Execeções)
# Ex1 

class Retangulo:
    def __init__(self, base, altura):
        if base <= 0: raise ValueError("A base deve der maior que zero")
        if altura <= 0: raise ValueError("A altura deve ser maior que zero")
        self._b = base 
        self._h = altura 
    
    def setBase(self, base):
            self._b = base

            
    def setAltura(self, altura):
            self._h = altura
            
    
    def getBase(self):
        return self_.b
    def getAltura(self):
        return self._h 
    
    def __str__(self):
        return f'A base do triangulo é {self._b} e altura {self._h}'
        
    def CalcArea(self):
        area = self._b * self._h
        return print(f'A área do seu retângulo é {area}')
        

try:
    base = int(input("Qual o valor da base do seu retângulo? "))
    altura = int(input("Qual o valor da altura do seu retângulo? "))
    retangulo = Retangulo(base, altura)
    
    print(retangulo)
    retangulo.CalcArea()
except ValueError:
    print(" Número ou base devem ser maior que zero  ")
    
    