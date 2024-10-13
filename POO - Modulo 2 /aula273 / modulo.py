def soma(x: float, y: float):
 return x + y


print(__name__) 
# Aqui vc percebe que caso execute
# vai aparecer __main__.

# Se importar o modulo.py para outro arquivo 
# e executar ele lá, o print aparece como "modulo" pois é o nome do arquivo
print(soma(12,3))