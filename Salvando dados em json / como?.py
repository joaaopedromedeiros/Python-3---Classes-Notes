# Posso usar qualquer tipo de dados, ou arquivo py! Nesse caso ele usou o dicionário apenas por ser mais complexo e mostrar que dá certo.

#1) add import json, no arquivo que deseja salvar os dados em json
#2) Vc utiliza o código with...


with open('tituloarquivo.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )

    # essa pessoa é a lista/tipodedado que vc deseja transformar em json 

#3) Como importar os dados do json pro python denovo?

with open('aula111.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)

    # print(pessoa)
    # print(type(pessoa)) --> veio em formato de dict, pois já era um né
    print(pessoa['nome']) --> importou o dados do json

 

# Obs: Funções,  métodos,  etc é mais complicado e não é bom salvar em json!  