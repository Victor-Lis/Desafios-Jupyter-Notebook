from classes.cachorro import Cachorro
from classes.gato import Gato
from classes.animal import Animal

gato = Gato("Whiskers")
cachorro = Cachorro("Rex")
animal = Animal("Animal Genérico")

print(f"{gato.nome} diz: {gato.fazer_barulho()}")
print(f"{cachorro.nome} diz: {cachorro.fazer_barulho()}")
try:
    print(f"{animal.nome} diz: {animal.fazer_barulho()}")
except NotImplementedError as e:
    print(e)