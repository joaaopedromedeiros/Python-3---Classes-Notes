# Abstração
class Log:
    def log(self, msg):
        raise NotImplementedError('Implemente o método log')
   # eu não quero que as pessoas use esse metodo diretamente, 
#  ai vc pede pra usar outro com o que vc informa na mensagem do erro

# raise --> implementar um erro pra teste

class LogFileMixin(Log):
    def log(self, msg):
        print(msg)
if __name__ == '__main__':
    l = LogFileMixin()
    l.log('qualquer coisa')