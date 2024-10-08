# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).

# Um ou muitos: Muitos produtos no carrinho de compras
# Diamante --> fechado a setinha 

class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos]) 

# Preço de cada produto "p" em self._produtos 

    def inserir_produtos(self, *produtos):
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto)

# *produtos = empacotar em tuple o que for passado 
# cada tupla de produto em produtos vc vai inserir sempre o novo >>em último append<<

    def listar_produtos(self):
        print() # só pra espaço 
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print() # só pra espaço 

# produto.nome e produto.preco --> definido na class Produto


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

# Agregar oq for passado em produto no carrinho 


carrinho = Carrinho() # Criou o carrinho
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20) # P1 e P2 respectivamente
 
carrinho.inserir_produtos(p1, p2)

carrinho.listar_produtos()

print(carrinho.total())