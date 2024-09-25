# Operadores lógico python

# and (e), or (ou), not (não)

# And - Todas condições precisam ser verdadeiras (+1 condição)
# Se qualquer valor for considerado falso a expressão inteira será avaliada
# naquele valor 

# São considerados falsy (que vc já viu)
# 0 0.0 ''(string vazia)  False --> se confrotado com boolean

# também existe o tipo de  dado >>None<< que é usado para representar um "não valor, nulo"

entrada = input("[E]ntrar ou [S]air: ")

senha_digitada = input("Senha: ")

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
  print('Entrar')
else: 
  print('Sair')

  # Para  entrar, todas  condições preciam ser verdadeiras = True. !!!!!
  # Se uma delas já for false, o resto nnem é avaliado.


print(True and True and True )
print(True and False and True ) # Avaliação de curto circuito
print(True and 0 and True ) # Avaliação de curto circuito
print(bool(0))
print(bool(0.0))
print(bool('')) # sem espaço, apenas as aspas. Se tiver esppaço já não vvai tá mais vazia e vai ser true

