class Teste:
    def __init__(self, x: str, y):
        self.x = f'Valor: {x}'
        self.y = y


p1 = Teste("1",2)

print(vars(p1))
print(p1.x)

