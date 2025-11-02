from classes.funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus
        
    def calcular_pagamento(self):
        return self.salario + self.salario * (self.bonus / 100)