# quociente & resto da divisão 

valor = int(input("Digite um valor inteiro: "))
dividir = int(input("Digite um número para dividir o valor anterior:  "))

def divisao(valor, dividir):
    quociente = valor // dividir
    resto = valor % dividir
    print(f'O resultado é {quociente} e resta {resto}')

divisao(valor,dividir)