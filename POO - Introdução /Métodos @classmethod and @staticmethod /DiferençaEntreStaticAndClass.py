# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None 
        self.password = None

# Olha que foda! Criei funções para setar esses valores, tipo criar comandos do minecraft

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

# Qualquer palavra que for usar self, é um método de instância! Precisa do self dentro do método? Instância 

# funções acima

# Situação abaixo: Criar um método que cria uma conexão que já recebe usuário e password, sem o self
# usa classmethod

# 1°) Não vamos ter acesso a self... pois já tá criado, 
# auth --> autenticar dados de usuário e senha  (authentication) 
# Quero acesso ao cls, a classe 

    @classmethod # então usa cls
    def create_with_auth(cls, user, password):
        connection = cls() # variável dentro do escopo do método 
        connection.user = user
        connection.password = password
        return connection




    @staticmethod
    def log(msg):
        print('LOG:', msg)


def connection_log(msg):
    print('LOG:', msg)


# c1 = Connection()
c1 = Connection.create_with_auth('luiz', '1234')
# c1.set_user('luiz')
# c1.set_password('123')
print(Connection.log('Essa é a mensagem de log'))
print(c1.user)