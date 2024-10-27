# média simples do aluno 

b1 = float(input("Digite a sua nota do 1° bimestre:"))
b2 = float(input("Digite a sua nota do 2° bimestre:"))
b3 = float(input("Digite a sua nota do 3° bimestre:"))


media_simples = (b1 + b2 + b3) / 3

if media_simples > 69:
    print(f" Sua média é {media_simples} e vc foi aprovado!")
elif media_simples >= 30 and media_simples <= 69:
    print(f" Sua média é {media_simples} e você está de recuperação")
elif media_simples < 30:
    print(f" Sua média é {media_simples} e você foi reprovado")



