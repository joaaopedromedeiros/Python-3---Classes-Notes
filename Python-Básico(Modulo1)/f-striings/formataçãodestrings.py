a = 'A'
b = 'B'
c = 1.1
string = 'a={} b={} c={:.2f}'

# {.2f}? Lembra de quando substituio com f string assim:
# >> f' Ola! {variável:.2f}' << 

#é a mesma coisa, mas o nome da variável alí ta oculto devido ter passado um parâmetro/argumento anteriormentee. 

formato = string.format(a, b, c) # Esses a, b, e c são argumentos/parâmetros relacionados com as variáveis

# Substituindo o 'a={} b} c{:.2f}' por uma única variável chamada string, tipo equação do 1° grau, apenas armazenei o valor:


#  Se aparecer out of range é porque "estar fora do alcance, ou seja, não existe esse valor que vc esta buscando. Isso é tipo por + {} sem ter colocado mais um argumento pra ser respectivamente o  valor dele"

# Tudo em python é objeto, ou seja, possui métodos dentro dele 

#  E se  eu quiser pegar um argumento epecífico? Usa os indíces. >>Começa do zero!!<< 
 
# Nessa situação eu não vou depender da ordem que coloco respectivamente mos argumentos, pois posso dizer  quem  vai ser o zero, ou qualquer  outro indice

string_atribuindo_indice = ' a={0} b={1} c={2:.2f}'
indice = string_atribuindo_indice.format(a,b,c)
print(indice)

# Obs: Os métodos de cada tipo dde dado apenas funcionam com eles mesmo. Mesmo que as variáveis com os valores  estejam ocultas se vc utilizar coisas/métodos que se aplicam apenas a 'str', por exemplo, vai da erro.

# Obs2: A partir do momento que eu coloco um parâmetro nomeado, eu preciso por todos os próximos

string_atribuindo_indice2 = ' a={nome1} b={nome2} c={nome3}'
indice2 = string_atribuindo_indice2.format(
  nome1=a,                                                                                             
  nome2=b,
  nome3=c)
print(indice2)

