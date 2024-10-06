# Lista 3 de POO
# Frete

class Frete:
    def __init__(self, distancia,peso):
        self._distancia = distancia
        self._peso = peso
        
        # garantir que o construtor vai setar os valores
        self.SetDistancia(distancia)
        self.SetPeso(peso)
    
    
    
    
    def SetDistancia(self, distancia):
        if distancia > 0:
            self._distancia = distancia
        else: raise ValueError("Distancia menor ou igual a zero")

        
    def SetPeso(self, peso):
        if peso > 0:
            self._peso = peso
        else: raise ValueError("Peso menor ou igual a zero")
        
    def GetPeso(self):
        return self._peso
        
    def GetDistancia(self):
        return self._distancia
    
    def CalcFrete(self):
        centavos = self._peso * self._distancia
        reais = centavos/100
        
        return f'O valor do frete é {reais}'
    def __str__(self):
        return f'Para a distância de {self._distancia}, e peso {self._peso}'

class UI:
    @staticmethod
    def main():
        distancia = int(input("Qual a distância? "))
        peso = int(input("Qual o peso da carga? "))
    
        frete = Frete(distancia, peso)
        print(frete)
        print(frete.CalcFrete())
    
UI.main()