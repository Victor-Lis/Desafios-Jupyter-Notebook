from classes.funcionario import Funcionario

class Vendedor(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        
    def calcular_bonus(self):
        return 1000