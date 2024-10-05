# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅

# Código abaixo

from abc import ABC, abstractmethod

# Por que abstrato? 
# A Notificação pode ser sms, email, WhatsApp,
# Notificação do próprio celular, cartorio. Então é abstrato. 
# Usamos esse from abc import ABC, abstractmethod
# Classe abstrata possui atributos similares com as filhas herdadas ( concretas )
# mas que tem funcionalidades diferentes dependendo da situação 
# ( Ex: FiguraPlana tem área indefinida com pass, Retângulo --> área definida ) 


class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem # isso é um atributo

    @abstractmethod
    def enviar(self) -> bool: ...

# Abstrato pois as subclasses que vão definir o tipo de notificação a ser enviada. 
# Obs²: Eu preciso utilizar essa classe abstrata em alguma concreta, passando através de herança (herdando de forma simples por exemplo).  
# Sem utilizar em classes concretas, vc não vai conseguir usar a abstrata ( abastrat: Tipo de atributo incerto ) 
# poderia ser:
# Notificação do próprio celular, cartorio. Então é abstrato. 




class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando - ', self.mensagem)
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.mensagem)
        return False


def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação NÃO enviada')


notificacao_email = NotificacaoEmail('testando e-mail')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('testando SMS')
notificar(notificacao_sms)


#OBSERVAÇÕES:

# >> Criando as classes filhas de notificação
# Quando herdei Notificação nas classes filhas eu 
# não utilizei o super().algumAtributoJáDefinidoAntes 
# Devido não ter nenhum anteriormente na classe abastrata e apenas
# Criamos o print para cada situação e o seu retorno

# >> -> bolean
# MUITO IMPORTANTE!
# Você está falando para o(a) dev que vai usar o dado
# verdadeiro ou falso no seu código a fim de executar algo

# >> Definindo tipo de dados de seu  parâmetros e seus argumentos, a fim de utilizar seu métodos internamente com funções
# def notificar(notificação: str):
#     notificação.upper()
# Obs¹: Caso passe algo diferente de string, isso apresenta error.

  