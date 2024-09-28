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
    global x
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao() # preciso declarar ela porque pra ter acesso a suas informações preciso chama lá na função maior ( >> escopo() <<)

    print(x)

# quando executar a escopo() vai chamar as duas.

# lembre-se, se vc criar uma variável no escopo global, vc pode acessar ela de qualquer lugar. Mas, se vc tiver um declarada/criada apenas dentro do escopo de uma função só é possível ser acessada lá.


print(x)
escopo()
print(x)