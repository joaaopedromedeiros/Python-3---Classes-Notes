# Herança Múltipla - Python Orientado a Objetos
# Quer dizer que no Python, uma classe pode estender
# várias outras classes.
# Herança simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Herança múltipla e mixins
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog) # múltipla Herança,  pessoa, filelog 
#
# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#
# método -> falar, D não tem o método mas entre B e C por aonde ele vai chamar?
#           A
#         /   \
#        B     C
#         \   /
#           D
# Problema do Diamante (acima), porque
# se eu quisr utikiza método dd C ou de B e eles forem igual, qual vai ser o caminho da ordem de chamada dos métodos? 

# Python 3 usa C3 superclass linearization
# para gerar o mro.
# Você não precisa estudar isso (é complexo)
# https://en.wikipedia.org/wiki/C3_linearization
#
# Para saber a ordem de chamada dos métodos
# Use o método de classe Classe.mro()
# Ou o atributo __mro__ (Dunder - Double Underscore)


# Resolvendo o problema do diamanete (parte 2 aula)

# Herança Múltipla - Python Orientado a Objetos
# Quer dizer que no Python, uma classe pode estender
# várias outras classes.
# Herança simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Herança múltipla e mixins
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)
#
# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#
# método -> falar
#           A
#         /   \
#        B     C
#         \   /
#           D
#
# Python 3 usa C3 superclass linearization
# para gerar o mro.
# Você não precisa estudar isso (é complexo)
# https://en.wikipedia.org/wiki/C3_linearization
#
# Para saber a ordem de chamada dos métodos
# Use o método de classe Classe.mro()
# Ou o atributo __mro__ (Dunder - Double Underscore)

class A:
    ...

    def quem_sou(self):
        print('A')


class B(A):
    ... # não pd deixar bloco vazio no python então coloca isso, ou também pode por pass

    # def quem_sou(self):
    #     print('B')


class C(A):
    ...

    def quem_sou(self):
        print('C')


class D(B, C): # A ordem de chamar obedece a ordem dos parâmetros ( vai em b dps o c e busca o método )
    ...

    def quem_sou(self):
        print('D')


d = D()
d.quem_sou()
# print(D.__mro__) --> ver ordem de aonde busca
print(D.mro()) # --> ver ordem de aonde busca

.