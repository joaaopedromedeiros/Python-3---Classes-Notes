class Contas:
    def __init__(self, a, b):
        self._a = a
        self._b = b
        
        self.setA(a) # o valor de A que pertence a instância criada no __init__ vai pra todos os self que tiver dentro do método __init__. inclusive se tiver essa função dentro dele. Ativa direto...
        self.setB(b)
        
    
    def setA(self, a):
        if a >= 0:
            self._a = a
        else: raise ValueError("Vc fez besteira em a")
        
    def setB(self, b):
        if b >= 0:
            self._b = b
        else: raise ValueError("Vc fez besteira em b")
    
    # Colocando em prática o setB, acima.
    # Cria função,  executa no __init__ com o self que já vai executar direto. 
        
        
    # gets
    def getA(self):
        return self._b
    
    def getB(self):
        return self._a
    
    def soma(self):
        return f'A soma é {self.getB() + self.getA()}' 
        
        # Usando get acima

#conta = Contas(1,2)
#conta_testeSetA = Contas(-1,2)
conta_testeSetB = Contas(1,-2)
print(conta_testeSetB.soma())
#print(conta.soma())


    

    