# Interpolação básica do string
# s - string
# d, i - int
# f - float
# x e X - hexadeciimal (ABCDEF#12345678)

nome = "Luiz"
preco = 1000.0000736382
variavel = '%s, o preço total é R$%.2f' % (nome,preco)
# (nome,preco), lembra do format, dá certo pois no parêntese ele dá a ordem e o python sabe quem é quem
print(variavel)

print("O hexadecimal de %d é %04x1" % (15,15) )

# Substitui ppelo o que vc define depois
# vc pode uusar f strings ou essa frma de interpolar (prefiiro f strings)


