# Função print

# \r\n --> CRLF --> Sistema de quebra de  linha do windows que vem padrão
# \n\ --> LF --> SISTEMA LINUX de espaço que vemm padrãoo

print(123, 45,"HelloWorld",True,False, sep=',', end='\r\n') 
print(123, 45,"HelloWorld",True,False, sep=',', end='##\n') #não é padrão

print(123,5555,"HelloWoooorld",True,False, sep=".", end="\n") 
#Função - (Argumentos,OutroArgumentoSeparadoPorVirgula)

# esse sep define como vai funionarr o separador. Vem com espaço como padrão

# O python é sensivel com as letras maiúsculos (Print não funciona,, mas prrint funciona)

#A maioria dos erros do python ele ja te corrige com o "did you mean: Palavra correta" no console

