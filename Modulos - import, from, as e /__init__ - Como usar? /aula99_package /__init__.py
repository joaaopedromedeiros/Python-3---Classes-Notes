from aula99_package.modulo import *
from aula99_package.modulo_b import *

#Resume
# 1) Cria uma pastanome
# 2) Cria esse __init__.py
# 3) Cria outros arquivos pra salvar funções, variáveis 
# 4) Importa esses arquivos pro __init__.py
# 5) Apenas por importar a pasta em algum arquivo 
# --> import pastanome
# eu vou conseguir utilizar todas funções, variáveis,  etc que estão salvas no __init__.py


# Observações MUITOOO IMPORTANTE:
# Em nenhum lugar eu importo esse __init__.py, eu só crio esse arquivo no package (na pasta). Pois esse arquivo vai fazer funcionar as funções,  variáveis e etc apenas importando a pasta.


# Como? Abaixo;
# >> import pasta_package << 

# E por ter dentro dessa pasta o __init__.py, o que tiver importado dentro desse __init__.py eu vou conseguir utilizar nos outros arquivos que eu fizer a importação dela.



# tudo que é importado para aqui e possível usar como o __algumacoisa__
# funções,  variáveis,  etc.

ex:

print(pasta_package.__algumacoisa__)



# nessa situação eu to importando todos os  arquivos para aqui.  Então aonde eu importar esse a pasta eu consigo usar!!!! como __AlgumaCoisa__


# E nos arquivos? Como usar após importar? 

from "pasta" import "oq-vc-quer", "oq-vc-quer3"
# depois é só usar 



