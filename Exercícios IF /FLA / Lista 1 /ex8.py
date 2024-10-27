dinheiro = float(input("Digite um valor em reais para comprar um bolo de 8.50: "))


bolo = 8.50 

compra = dinheiro // bolo
troco = dinheiro % bolo


if troco == 0.0:
    print(f'Você comprou  {compra} bolos e não possui troco')
elif troco != 0.0:
    print(f'Você comprou  {compra} bolos e restam {troco} de troco')
