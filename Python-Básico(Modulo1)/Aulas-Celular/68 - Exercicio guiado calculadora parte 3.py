""" Calculadora com while """
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    num_1_float = 0
    num_2_float = 0

    numeros_validos = None # uma flag 

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue #faz voltar pra reler 

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    

   print("Realizando o calculo")
   
   if operador == '+' :
   print(num_float_1 + num_float_2) 
   elif operador == '-': 
   print(num_float_1 - num_float_2) 
   elif operador == '*': 
   print(num_float_1 * num_float_2) 
   elif operador == '/': 
   print(num_float_1 / num_float_2) 
   

   

    ###

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break