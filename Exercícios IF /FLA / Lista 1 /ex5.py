# NÃO È 5, É A 7... o resto era só analisar e responder


a = int(input("Digite um número: "))
b = int(input("Digite um número: "))

try:
    maxima_divisao_inteira = a // b
    resto = a % b
    
    print(f'Quociente: {maxima_divisao_inteira}')
    print(f'Resto: {resto}')
except:
    print("Erro")
