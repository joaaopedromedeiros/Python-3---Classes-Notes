# Lista 4 de POO - Listas 4A
# Exercício 2

class Playlist:
  def __init__(self, nome, descricao):
    self._nome = nome
    self._descricao = descricao
    self._musicas = []

  def inserir(self, musica):
    return self._musicas.append(musica)

  #tempoTotal
  def Listar(self):
    return self._musicas # tava usando print(self._musicas) e quando dava print retornava none. Tirei e agr uso o for com o listar 
  
  def __str__(self):
    return f'A playlist {self._nome} tem como descrição {self._descricao}'
  
class Musica:
  def __init__(self, titulo, artista, album, dataInclusao, duracao):
    self._titulo = titulo
    self._artista = artista
    self._album = album
    self._dataInclusao = dataInclusao
    self._duracao = duracao

  def getTitulo(self):
    return self._titulo

  def __str__(self):
    return f'A música {self._titulo}, do {self._artista} do album {self._album}, incluida em {self._dataInclusao} tem duracação de {self._duracao}'


# Lógica do código

# Criar playlist, add música na playlist, listar música da playlist

class UI:
  @staticmethod
  def Main():

    op = 0
    created_playlist = 0
    musica_criada = 0

    while op == 0:
      menu = int(input("1 - Crie uma playlist, 2 - Adicione uma nova música,  3 - Liste todas as músicas da playlist, 4 - Sair do sistema"))

      if menu == 1:
        nome = input("Nome da playlist: ")
        descricao = input("Descrição da playlist? ")

        playlist = Playlist(nome, descricao)

        created_playlist += 1
        


        # Acabou de criar op continua sendo igual a zero, ele retorna pro começo
      if menu == 2:
        if created_playlist == 1:
          titulo = input("Qual o nome da música? ")
          artista = input("Qual o nome do artista? ")
          album = input("Qual o nome do album da música? ")
          dataInclusao = input("Qual a data de inclusão? ")
          duracao = input("Qual a data de duracação da música? ")
        
          musica = Musica(titulo, artista, album, dataInclusao, duracao)

          playlist.inserir(musica)
          print()
          print("Playlist atualizada: ")
          for id, musica in enumerate(playlist.Listar(), 1):
            print(f'{id}, {musica.getTitulo()}')
            musica_criada += 1


        else: print("Você precisa criar uma playlist antes")

      if menu == 3:

        if musica_criada == 1:
          print("Confira sua lista atual: ")
          for id, musica in enumerate(playlist.Listar(), 1):
            print(f'{id}, {musica.getTitulo()}')
        else: print("Você precisa criar pelo menos uma música")
      if menu == 4:
        print("Saindo do sistema...")
        break
      
    



UI.Main()



