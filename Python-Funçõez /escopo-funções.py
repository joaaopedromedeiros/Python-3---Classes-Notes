8
"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1


def escopo():
    #global x --> faz o x se tornar editável no scopo global
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao() # preciso declarar ela porque pra ter acesso a suas informações preciso chama lá na função maior ( >> escopo() <<)

    print(x)

# quando executar a escopo() vai chamar as duas.

# lembre-se, se vc criar uma variável no escopo global, vc pode acessar ela de qualquer lugar sem alterar o valor global e só nela. Mas, se vc tiver um declarada/criada apenas dentro do escopo de uma função só é possível ser acessada lá (precisa declarar ela antes no global).

# Obs²: o x definido no escopo global !=  (diferente) do x do escopo!!! Os valores, etc... nenhuma alteração da variável do escopo vai influenciar na global. Ao nenos que use
# global "variável"

# Obs: mesmo que o x do escopo global não seja acessivel nos escopos das funções eu preciso criar ela no global antes de chamar a é função() se n dá erro de variável n criada.


# variáveis  de dentro pedindo pra variáveis de fora eu tenho acesso, mas de fora pedindo acesso as de dentro n tenho acesso

print(x) # x = 1
escopo() # x = 10 escopo 1, 11 escopo 2
print(x) # x = 1