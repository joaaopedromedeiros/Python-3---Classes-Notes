# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# Para utilizar eles vcs precisam ssber a sssinatura dele, quantos objetos preciso? 
# self -> 1 objeto
# self and other ( +1 objeto) 



# __lt__(self,other) - self < other
" acima, checa se um objeto é menor ou igual "

# __le__(self,other) - self <= other
" menor ou igual que outro objeto "

# __gt__(self,other) - self > other
" greater than... maior que outro objeto "

# __ge__(self,other) - self >= other
" greatest or equal, maior ou igual a outro objeto 

# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str

# É basicamente comparações entre objetos de acordo com os sinais comparativos