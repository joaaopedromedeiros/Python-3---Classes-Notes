# Flag (Bandeira) - Marcar um llocal
#None  - Nãoo  valor
# is e is not = é ou não é (tipo,valor, idetidade)


# id = identidade

v1 = 'a'
v2 = 'b'
print(id(v1))
print(id(v2))

# is e is not = é ou não é (tipo,valor, idetidade)


condição = False

passou_no_if = None

if condição:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if is None)
print(passou_no_if is not None) 

# No momento que n for "None" o valor da variável essa condição vai ser verdade (a afirmação do valor não ser none é verdade)




