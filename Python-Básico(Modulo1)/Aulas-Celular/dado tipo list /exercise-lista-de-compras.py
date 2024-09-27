# A did it ;)

print("Bem vindo a sua lista de compras!")

# apagar, inserir e listar valores da lista

lista = []

while True: 
    add_item = \
    input("Adicione o seu item a lista: ")
    
    if add_item != " ":
       lista.append(add_item)
       print("                            ")
       
       print(f'{add_item} foi adicionado com sucesso! Confira abaixo sua lista')
       
       print("                            ")
       
       print("                            ")
       
       print("Sua lista atual é")
       for indice,item in enumerate(lista):
           print(f' ID: {indice} Item: {item}')
       
       print("                            ")
       
       menu = input("Você deseja adicionar outro item ou remover? Escreva add ou remover: ")
       
       if menu == 'add':
           continue
       else: 
           remover = int(input("Digite o ID do item que deseja remover: "))
           del lista[remover]
           print("Lista atualizada! Confira")
           print(lista)
       
       
    
    
    
    





