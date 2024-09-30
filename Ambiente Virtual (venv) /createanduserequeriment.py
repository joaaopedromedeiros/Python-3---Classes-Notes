# pip uninstall nome_pacote
# Congelar (ver pacotes)
# pip freeze
#
# Criando o arquivo e usando um requirements.txt
# pip freeze > requirements.txt

# Instalando tudo do requirements.txt
# pip install -r requirements.txt

# Como atualizar com novos pacotes que coloquei no projeto? Para atualizar isso com os novos e manter os antigos é só fazer a mesma coisa novamente 

pip freeze > requirements.txt


# OBSERVAÇÃO 

# Vc manda isso pro github pois mandar todos pacotes que vc instalou direto pode ficar enorme. Ai ele lista tudo e vc baixa na hora 

# Em todo projeto que não tiver o venv e tiver o requirements.txt, vc abre a pasta do projeto, cria o ambiente virtual novo e chama o requirments com o pip que vai automaticamente instalar tudo que precisa