# Introdução ao try/expect
# try --> tentar executar o código
# except --> ocorreu algum erro ao tentar executar o código

# Mesma coisa do try catch do javascript. 

print(123)
print(456)

# o python vai parar aqui assim que executar o erro ("a" para número), então vaii aparecer uma exceção de erro pois não dá 

# int('a'), tira o # para ver o erro se  quiser

# >> Outtro exemplo de erro

numero_str = input("Vou dobrar o número que vc digitar: ")

# Como conferir se é digito inteiro (True or False)?
print(numero_str.isdigit())

# >>>>>> Código com if <<<<<<<





# if numero_str.isdigit():
#2  numero_float = float(numero_str)
  # correção do erro (acima)
#  print(f'O dobro de {numero_str} é {numero_float * 2}')
#else:
#  print("O número que vc digitou não é um digito")


# >> Como ambos são strings appenas colocou 1 no lado do outro. Por isso o int()


# >>>>>>  Fim Código com if <<<<<<<


  # O if não evita erros de acontecerem. O try sim... se ali deu problema para na hora todo o código.

  

try:
  print('STR:', numero_str)
  numero_float = float(numero_str)
  print('FLOAT:', numero_float)
  # correção do erro (acima)
  print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
  print('Isso não é um número')

  # Captura o erro, e não ppara todo o código.



