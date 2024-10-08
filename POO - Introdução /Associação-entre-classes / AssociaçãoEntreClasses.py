# Relações entre classes: associação, agregação e composição

# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.

# O escritor usa a ferramenta


# Site para desenhar d. drawio, diagrams net 


class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property 
# Criando o atributo separado
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter 
# Adicionando pra conseguir atribuir na variável 
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, nomeferramenta):
        self.nomeferramenta = nomeferramenta

    def escrever(self):
        return f'{self.nomeferramenta} está escrevendo'


# Classe 1 
escritor = Escritor('Luiz')

# Classe 2 (1° Ferramenta)
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Máquina')

# Associação das classes abaixo: 

escritor.ferramenta = maquina_de_escrever # o self.nomeferramenta = maquina que foi atribuido 

#escritor.atributoCriado = algo 
# Definindo ferramenta (atributo property 
# de escritor) escrito com outra classe 


# Print do resultado

print(caneta.escrever())
print(maquina_de_escrever.escrever())
print(escritor.ferramenta.escrever())
     
# E esse .ferramenta? É do @property que transforma o método/função em "atributo" e usa em ().