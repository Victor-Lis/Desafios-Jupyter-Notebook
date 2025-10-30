from jogador import Jogador

class JogadorLinha(Jogador):
    def __init__(self, nome, idade, posicao):
        super().__init__(nome, idade)
        self.posicao = posicao

    def __str__(self):
        return f"{self.nome} ({self.idade} anos): {self.posicao}"