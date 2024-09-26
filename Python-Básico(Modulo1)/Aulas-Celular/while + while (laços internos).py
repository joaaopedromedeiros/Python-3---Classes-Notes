# O while ele funciona da da seguinte forma
# Ele executa um bloco while até que a condição se torne verdadeira. Isso, siginifica que...

# Um while(a) dentro de outro while(b), vai passar por while(b), vai pro (a) e só vai voltar pro while(b) quando ele for verdadeiro.

# ele primeiro executa todo while(a) pra se tornar verdadeiro, e só dps retorna pro while maior.

se eu tiver:


"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

qtd_linhas = 5
qtd_colunas = 5
linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1
print('Acabou')


