from jogador import Jogador

class Goleiro(Jogador):
  def __str__(self):
    return f"O goleiro {self.nome} tem {self.idade} anos"

  def agarrar(self):
    print(f"{self.nome} agarrou!")