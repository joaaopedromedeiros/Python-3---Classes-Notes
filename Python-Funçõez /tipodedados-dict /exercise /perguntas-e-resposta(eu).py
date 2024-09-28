# Pergunta 1 

pergunta1_validacao = True
while pergunta1_validacao == True: 
    alternativas = ['1', '3', '4', '5']
    pergunta_1 = input(f'Quanto é 2+2? De acordo com as alternativas abaixo {alternativas}? ')
    
    
    if pergunta_1 == '4':
        print('Resposta correta!')
    else:
        print('Tente novamente')
        continue
    
    pergunta1_validacao = False
    
    print("                     ")
    
pergunta2_validacao = True
while pergunta2_validacao == True: 
    alternativas2 = ['25', '55', '10', '51']
    pergunta_2 = input(f'Quanto é 5*5? De acordo com as alternativas abaixo {alternativas2}? ')
    
    
    if pergunta_2 == '25':
        print('Resposta correta!')
    else:
        print('Tente novamente')
        continue
    
    pergunta2_validacao = False
   
pergunta3_validacao = True
while pergunta3_validacao == True: 
    alternativas3 = ['4', '5', '3', '2']
    pergunta_3 = input(f'Quanto é 10/2? De acordo com as alternativas abaixo {alternativas3}? ')
    
    
    if pergunta_3 == '5':
        print('Resposta correta!')
    else:
        print('Tente novamente')
        continue
    
    pergunta3_validacao = False
    
    print("Parabéns todas respostas foram respondidas corretamente!")

    
    
    






# Anotações 

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]