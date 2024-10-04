class FigmaProject:
    def __init__(self, projectname, team, date, status):
        self.__projectmame = projectname
        self.__team = team
        self.__date = date
        self.__status = status 
        
    # Criando atributos "property"
    def SetName(self, projectname):
        self.__projectname = projectname
        
    def SetTeam(self, members):
        self.__team = members
    
    def SetDate(self, date):
        self.__date = date
    
    def SetStatus(self, status):
        self.__status = status
        
    # Criando return "setter"
    
    def GetName(self, projectname):
        return self.__projectname
        
    def GetTeam(self, members):
        return self.__team
    
    def GetDate(self,date):
        return self.__date
    
    def SetStatus(self, status):
        return self.__status
        
    # usando o mètodo str na instância que ela for chamadaaaa, assim vejo os dados dentro do dict
    
    def __str__(self):
        return f'{self.__projectname}, {self.__team}, {self.__date}, {self.status}'
        
        # consertar isso
        
    

# Os inputs eles rodam mesmo dentro da classe

projectname = input("Qual o nome do projeto?")
team = input("Quem desenvolve o projeto")
date = input("Qual data é hoje?")
status = input("Qual o nivel de desenvolvimento?")

try:
    p = FigmaProject(projectname, team, date, status)
    print(vars(p))
    print(p)
except ValueError as error:
    print(error)
        
        
        
        

# Quero criar o projeto, setar o nome, setar o desenvolvedor, data criada, e % de desenvolvimento. 