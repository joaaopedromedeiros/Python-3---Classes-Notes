from log import LogFileMixin
class Eletronico:

    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            self._ligado = False

class Smartphone(Eletronico, LogFileMixin):
    def ligar(self):
        super().ligar() # super pra pegar as primeiras funcionalidades e conseguir add mais

        if self._ligado:
            msg = f'{self._nome} está ligado'
            self.log_success(msg)
    

   def desligar(self):
        super().desligar() # " mesma coisa de acima "
        if not self._ligado:
            msg = f'{self._nome} está desligado'
            self.log_error(msg)