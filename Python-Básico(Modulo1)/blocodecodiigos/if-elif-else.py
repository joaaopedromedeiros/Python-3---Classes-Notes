# Condicionais

# if - / elif /  - else
# se - / se  não se /- se  não

entrada = input('Você quer "entrar" ou "sair"? ')

# print('Você entrou no sistema')
# print('Você saiu do sistema')

# Para executar essafunção vai precisar do IF, que vai ser de acordo com uma informação em (boolean), true ou false

if entrada == 'entrar':
  print('Você entrou no sstema (bloco de codigo 1)')
elif entrada == 'sair':
  print('Você saiu do sistema, (bloco de codigo 2)')
elif entrada == 'Nao':
  print('Nao')
else: 
  print('Você não digitou entrar  nem sair (bloco de codigo 3)')

# posso repetir o elif com váias condições, e posso ter vários trechos de código dentro de um bloco da condição

print("Fora dos blocos")
