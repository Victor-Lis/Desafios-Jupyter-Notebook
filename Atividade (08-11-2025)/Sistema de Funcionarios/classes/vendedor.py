from classes.funcionario import Funcionario

class Vendedor(Funcionario):
    def __init__(self, nome, salario, comissao):
        super().__init__(nome, salario)
        self.comissao = comissao
        
    def calcular_pagamento(self):
        return self.salario + self.comissao