from classes.veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
    
    def calcular_ipva(self):
        return 180