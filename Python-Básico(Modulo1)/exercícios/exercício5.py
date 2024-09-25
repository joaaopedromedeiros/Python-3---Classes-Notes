digite = input("Digite um número inteiro")


if digite.isdigit():
  digite_int = int(digite)
  par_ou_impar = digite_int % 2 == 0
  par_ou_impar_texto ='impar'
  
  if par_ou_impar is True:
    par_ou_impar_texto = 'par'
    print(f'O número {digite_int} é {par_ou_impar_texto}')
  else:
    print("Você não digitou um número inteiro")

horario = input("Qual o horário? ")
horario_para_int = int(horario)

if horario_para_int > 0  and horario_para_int < 11  :
 print(f"Bom dia, são {horario_para_int}")

elif horario_para_int > 12 and horario_para_int < 18  :
 print(f"Boa tarde, são {horario_para_int}")
 2
elif horario_para_int > 18 :
 print(f"Boa noite, são {horario_para_int}")


nome_do_usuario = input('Escreva seu primeiro nome: ')

if len(nome_do_usuario) < 4:
  print("Seu nome é curto")
elif len(nome_do_usuario) > 5:
  print("Seu nome é normal") 
elif len(nome_do_usuario) > 6:
  print("Seu nome é muito grande")
