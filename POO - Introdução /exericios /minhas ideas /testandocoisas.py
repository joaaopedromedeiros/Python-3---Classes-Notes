class Teste:
    def __init__(self, x: str, y, p, usandoinput=None):
        self.x = f'Valor: {x}'
        self.y = y
        self._UsarProperty = p
        self.ValorInput = usandoinput
    
    
    def set_Property(self, algo):
        self.UsarProperty = algo
    
    def get_Property(self, algo):
        return self.UsarProperty
        
usandoinput = input('Digite o valor que vai assumir o argumento do parâmetro "usandoinput" ')
    
    
    
        
    


p1 = Teste("1",2,3, usandoinput)

print(vars(p1))
print(p1.x) # posso ver o valor 
print(p1.UsarProperty)

# p1.UsarProperty("Ola")  
#não posso fazer passar valor assim. 
# Logo eu uso property e setter 
# (ou defino e retorno eles)

# Usando "property/setter" eu substitui

p1.set_Property("IssoAi")
print(p1.UsarProperty)


print(p1.ValorInput)






