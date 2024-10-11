# Lista 7 -  Dicionário de classes

class Client:
    def __init__(self, id: int, nome: str, email: str, fone: str):
        self._id = id
        self._nome = nome
        self._email = email
        self._fone = fone
    # sets
    def setId(self, id):
        self._id = id

    def setNome(self, nome):
        self._nome = nome

    def setEmail(self, email):
        self._email = email

    def setFone(self, fone):
        self._fone = fone
    
    #gets
    def getId(self):
        return self._id
    
    def getNome(self):
        return self._nome
    
    def getEmail(self):
        return self._email
    
    def getFone(self):
        return self._fone
    
    def __str__(self):
        return f'Id: {self.getId()}, Nome: {self.getNome()}, Email: {self.getEmail()}, Telefone: {self.getFone()}  '


#clientee = Client(1,"JOAO","SMAIL","123456")
#print(clientee)

class Agenda:
    def __init__(self, id, data, confirmado, idClient, idServico):
        self._id = id
        self._data = data
        self._confirmado = confirmado
        self._idClient = idClient
        self._idServico = idServico
    # sets
    def setId(self,id):
        self._id = id

    def setData(self,data):
        self._data = data

    def setConfirmado(self,confirmado):
        self._confirmado = confirmado

    def setIdClient(self,idClient):
        self._idClient = idClient

    def setidServico(self,idServico):
        self._idServico = idServico

    # gets
    def getId(self):
        return self._id
    
    def getData(self):
        return self._data
    
    def getConfirmado(self):
        return self._confirmado
    
    def getClient(self):
        return self._idClient
    
    def getServico(self):
        return self._idServico
    
    def __str__(self):
        return f'Agenda: ID - {self.getId()}, Date - {self.getData()}'
    

class Servico:
    def __init__(self, id, descricao, valor, duracao):
        self._id = id
        self._descricao = descricao
        self._valor = valor
        self._duracao = duracao
    
    #sets
    def setId(self,id):
        self._id = id
    def setDescricao(self, descrição):
        self._descricao = descricao
    def setValor(self, valor):
        self._valor = valor
    def setDuracao(self, duracao):
        self._duracao = duracao
    #gets
    def getId(self):
        return self._id
    def getDescricao(self):
        return self._descricao
    def getValor(self):
        return self._valor
    def getDuracao(self):
        return self._duracao
    
    def __str__(self):
        return f''
    
    


    
