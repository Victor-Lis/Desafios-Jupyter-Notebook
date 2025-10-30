from jogador_linha import JogadorLinha
from goleiro import Goleiro

jogador1 = JogadorLinha("Victor", 18, "ATA")

try:
  jogador1.agarrar()
except AttributeError as e:
  print(e)  

print(jogador1)

jogador2 = Goleiro("Weverton", 36)
try:
  jogador2.agarrar()
except AttributeError as e:
  print(e)  

print(jogador2)

# jogador1.passar()
# jogador1.chutar()