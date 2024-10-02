# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯

class Caneta:
    def __init__(self, cor):

        # private protected
        self.cor = cor
        self._cor_tampa = None

# >>>>>>>>>>
# se tiver "_" antes de algo como ._cor é uma
# convenção entre devs que não se pode modificar esse
# atributo  ( 1 ou 2 --> "_" ou "__" )
# NÃO DEVEM SER USADOS FORA DA CLASSE, NEM EM PRINT, NEM EM NADA... SÓ PD AQUI
#>>>>>>>>>

# Não use oq disse acima, use como se fosse atributo isso abaixo 

    @property 
# aqui é só um método que parece se comportar como atributo "caneta.cor = algo >> dá errado pois é um método <<<
# Vc pd usar como atributo, como ta nas 2 primeiras linhas com instância e print 

    def cor(self):
        print('ESTOU NO GETTER')
        return self._cor

# abaixo: Aqui vc usa atribuindo valor mesmo devido ter o cor.setter 

    @cor.setter
# assim posso atribuir no codigo, pois dá opção de setter 
# aqui salva valor com o setter

    def cor(self, valor):
        print('ESTOU NO SETTER')
        self._cor = valor

# Property = getter  (pega informação)

    @property
    def cor_tampa(self):
        return self._cor_tampa

# Setter = Libera atribuir dados manualmente
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Azul')
print(caneta.cor)

# Depois do setter 

caneta.cor = 'Rosa'
caneta.cor_tampa = 'Azul'

print(caneta.cor)
print(caneta.cor_tampa)