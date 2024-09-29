# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set): # set --> tipo de dado
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

# a partir do momento que o vscode percebe o tipo de dado ele já oferece os métodos daquele tipo, como o item.add que é possível usar com o set().

    elif isinstance(item, str):
        print('STR')
        print(item.upper())

# já oferece o upper das strings... pois reconheceu 


    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)
    else:
        print('OUTRO')
        print(item)


# sem checar com isistance o código provavelmente quebraria pois não teria como aplicar todos os métodos pra tudo, pois upper não funciona com set, ou add não funciona com string.