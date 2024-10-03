# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros


# 5 - Faça a ligação entre Carro e um Fabricante 
# Obs.: Um fabricante pode fabricar vários carros

# Exiba o nome do carro, motor e fabricante na tela

# Eu usei setter aqui, não associei


class Carro:
    def __init__(self, modelo):
        self._modelo = modelo
        self._fabricante = None
        self._motor = None
    
    @property
    def definir_motor(self):
        return self._motor
        
    # Property apenas o self + oq retorna
    
    @definir_motor.setter
    def definir_motor(self, motor):
        self._motor = motor
    
    # self, param + 
    # variavel = param/argumento, sem return
    
    
    @property
    def set_fabricante(self):
        return self._fabricante
    
    
    @set_fabricante.setter
    def set_fabricante(self, marca):
        self._fabricante = marca
    
    
    def showcar(self):
        print(f'Carro é {self._modelo}, fabricante {self._fabricante} com motor {self._motor}')
    
    
        

        

# 

camaro = Carro("Camaro")
camaro.definir_motor = "V10"
camaro.set_fabricante = "Chevrolet"
camaro.showcar()

# Abaixo é o que a função faz  
# modelocarro = camaro._modelo
# print(modelocarro)
# Conclusão: self --> instância/camaro

print(vars(camaro))