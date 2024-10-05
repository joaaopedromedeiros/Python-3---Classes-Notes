# Levantando e tratando suas Exceptions (Exceções)
# https://docs.python.org/3/library/exceptions.html

# Levantando (raise) / Lançando (throw --> js) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

# CÓDIGO ABAIXO


class MeuError(Exception):
    ...

class OutroError(Exception):
    ...
def levantar():
    exception_ = MeuError('a', 'b', 'c')

# Devido querer enviar +1 dado de error criei 
# essa tupla que vai chegar em forma de dados ->
# fornato de  args.

    raise exception_

# Esse tipo de função NUNCA RETORNA algo, essas que utilizam RAISE

# >> Sobre o Try:
# Imagina que vc tem uma bola e quer relançar o
# erro no sistema. Vc faz assim: 

try:
    #1/0  --> se tirar isso aparece que foi Division error no primeiro print e msg padrão desse erro
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__) # Ver a classe que foi ativada com o erro
    print(error.args)
    print()
    exception_ = OutroError('Vou lançar de novo')
    raise exception_ from error


# Após o excepct o error está sendo tratado


# OBSERVAÇÕES

# >> dinâmica simples do raise.
# def levantar():
#   raise meuError("A mensagem do meu erro")
# Apenas de chamar isso dá erro
# No código acima a dinâmica é a mesma mas chamou variável exception_ que possui a classe...

# >> Comece a ler o traceback
# Confira o passo a passo do erro

# >> Observações except, revisão
# try:
#    levantar()
# except (MeuError, ZeroDivisionError) as error:
#    print(error.__class__.__name__)
#    .... resto do código
# esse trecho: except (...) as error, basicamrnte
# criou uma variável error para armazenar os dois
# tipos de erros mencionados.

# >> Como eu passei esses args para meuError?
#  exception_ = MeuError('a', 'b', 'c')
# o meuError é uma classe:
# class meuError(exception):
#   pass
# Então: nesse parâmetro exception ele suporta passar esses argumentos. Por esse motivo o que é
# passado neles viram dados.
# Por isso posso usar error.args 

# >> Error ZeroDivisionError
# Erro padrão do python