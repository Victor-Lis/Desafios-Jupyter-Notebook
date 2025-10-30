class Jogador:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def passar(self):
    print(f"{self.nome} passou a bola!")

  def chutar(self):
      print(f"{self.nome} chutou a bola!")