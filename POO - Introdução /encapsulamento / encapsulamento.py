# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso

# Mas podemos seguir as seguintes convenções

#   (sem underline) = public
#   pode ser usado em qualquer lugar
# >> Métodos e self.algo


# _ (um underline) = protected
# não DEVE ser usado fora da classe
# ou suas subclasses.
# >>> _Métodos e self_algo


# __ (dois underlines) = private
# Não pode ser usado nas classes filhas!
# >>>> __Métodos e self__algo 

# Obs: protected & private podem ser utilizado em qualquer lugar DENTRO DA CLASSE.



#       "name mangling" (desfiguração de nomes) em Python

#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.
from functools import partial


class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'

# não acesse/use isso no código com print, variáveis,  etc. Use apenas dentro da classe 

        self.__exemplo = 'isso é private'

    def metodo_publico(self):
        # self._metodo_protected()
        # print(self._protected)

# >>> Você pd usar esse método _protected em qualquer da SUA CLASSE mas fora dela não, por isso posso chamar ela no método público mas dentro da classe. 

        print(self.__exemplo)
        self.__metodo_private()
        return 'metodo_publico'

    def _metodo_protected(self):
# Apenas utiliza dentro da classe,  não chama ela fora! 

        print('_metodo_protected')
        return '_metodo_protected'

    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'


# Fora da classe (tudo que ta abaixo) abaixo

f = Foo()
# print(f.public)
print(f.metodo_publico())