reais = float(input("Digite o valor para comprar o bolo que custa 8.50: "))


# 8.50, quero o troco

def bolo(reais):
    comprar = reais // 8.50
    print(f'Você pode comprar {comprar} bolos')
    troco = reais % 8.50
    print(f'Você tem {troco} reais de troco')


bolo(reais)
    
    
    