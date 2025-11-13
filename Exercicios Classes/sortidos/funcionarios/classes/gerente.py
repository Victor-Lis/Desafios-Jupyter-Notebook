from classes.funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        
    def calcular_bonus(self):
        return self.salario * 0.25 + 2000.0