import datetime
# Lista de POO (Exceções)
# paciente (Ex2)





 ( NÃO FINALIZEI, FALTA ESTUDAR COMO FUNCIONA O TEMPO DATETIME... ) 






class Paciente:
    def __init__(self, nome, nascimento, telefone, cpf):
        if nascimento > datetime.datetime.today(): raise ValueError("A data de nascimento precisa ser antes da data de hoje")
        self.__nome = nome
        self.__nascimento = nascimento
        self.__telefone = telefone
        self.__cpf = cpf
        
        def __str__(self):
            return f'O nome do paciente é {self.__nome}, nasceu em {self.__nascimento}, telefone para contato: {self.__telefone} e possui CPF: {self.__cpf}'

nome = input("Nome do paciente: ")
nascimento_txt = input("Digite a sua data de nescimento: ")
nasc = datetime.datetime.strptime(nascimento_txt, '%d/%m/%Y')
cpf = input("Digite o seu cpf: ")
telefone = input("Digite o seu número para contato: ")


# 
try: 
    pacientee = Paciente(nome, nascimento_txt, cpf, telefone)
    print(Paciente)
    
except ValueError as error:
    print(error)
    
    
            
    