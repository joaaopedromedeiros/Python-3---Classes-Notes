from aula99_package.modulo import *
from aula99_package.modulo_b import *



# Observações MUITOOO IMPORTANTE:
# Em nenhum lugar eu importo esse __init__.py, eu só crio esse arquivo no package (na pasta). Pois esse arquivo vai fazer funcionar esses ngc que mencionei acima apenas importando, por exemplo, pasta_package, sem especificar o arquivo.

# Como? Abaixo;
# >> import pasta_package << 

# E por ter dentro dessa pasta (pasta_package) o __init__.py, o que tiver importado dentro desse __init__.py eu vou conseguir utilizar nos outros arquivos que eu fizer a importação como citado acima.



# tudo que é importado para aqui e possível usar como o __algumacoisa__
# funções,  variáveis,  etc.

# nessa situação eu to importando todos os  arquivos para aqui.  Então aonde eu importar esse a pasta eu consigo usar!!!! como __AlgumaCoisa__



