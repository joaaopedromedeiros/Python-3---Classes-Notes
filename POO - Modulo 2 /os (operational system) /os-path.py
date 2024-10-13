# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. 

# Desse modo,
# Define o nome das pastas e arquivos que precisa acessar sem se preocupar com o sistema ( se è \ ou /): 

# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria

# Independente do sistema operacional iria adaptar como acessar as pastas: 

# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.


# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
#              diretorio.     arquivo

# os.path.exists: verifica se um caminho especificado existe.

# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.


import os
caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
# print(caminho)
diretorio, arquivo = os.path.split(caminho)
# Como da split, vc separa e vira tupla com 2 coisas e abaixo eu criei 2 variáveis 

nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
# nome_arquivo assume o valor da 1 tupla
# e a extensao_arquivo é o outro valor da tupla


# print(nome_arquivo, extensao_arquivo)
# print(os.path.exists('/Users/luizotavio/Desktop/curso-python-rep'))
# print(os.path.abspath('.'))
print(caminho)
print(os.path.basename(caminho))
print(os.path.basename(diretorio))
print(os.path.dirname(caminho))