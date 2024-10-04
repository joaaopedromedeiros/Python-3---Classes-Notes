# Abstração
class Log:
    def log(self, msg):
        raise NotImplementedError('Implemente o método log')
   # eu não quero que as pessoas use esse metodo diretamente, 
#  ai vc pede pra usar outro com o que vc informa na mensagem do erro
# não quer que vc use a super classe, a classe mãe.  Ai vc implementa erro e diz a classe que deve usar que é filha dessa super classe ( herda os dados, etc ) 
# raise --> implementar um erro pra teste

class LogFileMixin(Log):
    def log(self, msg):
        print(msg)
if __name__ == '__main__':
    l = LogFileMixin()
    l.log('qualquer coisa')