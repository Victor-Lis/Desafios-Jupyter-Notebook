from classes.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, potencia_cv):
        super().__init__(marca, modelo, ano)
        self.potencia_cv = potencia_cv
    
    def calcular_ipva(self):
        return (self.potencia_cv * 10) + 150