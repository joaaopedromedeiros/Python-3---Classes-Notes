# parte 1

"""
CONSTANTE = Variáveis que não vão mudar
Muitas condições no mesmo if (ruim)
 <<  contagem de commplexidade
"""

velocidade_carro = 61 #velocidade atual do carro
local_carro = 99 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar  pega

# CONSTANTES COM LETRAS MAIÚSCULAS NO PYTHON NÃO VÃO MUDAR NO CÓDIGO, CONVENÇÃO. 
# QUUANTO MAIS AFAASTADO DA LINHA (+ESPAÇO) MAIS COMMPLEXO FICA...
#            print('...')













#parte 2 - exercício

# cOLOCANDO CONDIÇÕES  EMM VARIÁVEIS PARA DEIXAR ELLAS MAIS LEGIVEIIS. VAi colocando as condições dentr de variável.

velocidade_carro_passar_radar_1 = (velocidade_carro > RADAR_1)

carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
local_carro <= (LOCAL_1 + RADAR_RANGE) 

if  velocidade_carro_passar_radar_1 :
  print("Velocidade carro passou radar 1")



if carro_multado_radar_1 and velocidade_carro_passar_radar_1 :
  print('Carro multado em radar 1')