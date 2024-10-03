# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros


# 5 - Faça a ligação entre Carro e um Fabricante 
# Obs.: Um fabricante pode fabricar vários carros

# Exiba o nome do carro, motor e fabricante na tela


class Carro:
    def __init__(self, modelo):
        self._modelo = modelo
        self._motor_carro = None
        self._fabricante_carro = None
        
    # Property e setter para setar os dados obtidos nas classes abaixo
    
    # Criando set_motor
    @property
    def set_motor(self):
        return self._motor_carro
        
    @set_motor.setter
    def set_motor(self, motor):
        self._motor_carro = motor
        
    #Criando set_fabricante
    
    @property
    def set_fabricante(self):
        return self._fabricante_carro
    
    @set_fabricante.setter
    def set_fabricante(self, empresa):
        self._fabricante_carro = empresa
    
    def carprofile(self):
        print(f'O seu carro é {self._modelo}')
    
    
    
    
# Criando classes para criar características 
class Motor:
    def __init__(self, motor):
        self.motor = motor


class Fabricante:
    def __init__(self, fabricante):
        self.fabricante = fabricante
        
    
    

    
    
        
# Fora do código
    
uno = Carro("uno")
motor_fiat = Motor("V10")
fabricante_fiat = Fabricante("fiat")

print(vars(motor_fiat))
print(vars(fabricante_fiat))



# Definindo as características do uno (associando classes)

# uno.set_motor = "V10"  --> funciona
# então:

uno.set_motor = motor_fiat
uno.set_fabricante = fabricante_fiat
uno.carprofile()

print(uno.set_fabricante)

# print(vars(uno)) --> tire o # e veja que tá sentando corretamente 








