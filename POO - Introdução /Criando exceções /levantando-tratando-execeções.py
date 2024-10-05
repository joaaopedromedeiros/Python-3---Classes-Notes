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
    raise exception_

# Esse tipo de função NUNCA RETORNA algo, essas que utilizam RAISE


try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError('Vou lançar de novo')
    raise exception_ from error

# OBSERVAÇÕES

# >> dinâmica simples do raise.
# def levantar():
#   raise meuError("A mensagem do meu erro")
# Apenas de chamar isso dá erro
# No código acima a dinâmica é a mesma mas chamou variável exception_ que possui a classe...