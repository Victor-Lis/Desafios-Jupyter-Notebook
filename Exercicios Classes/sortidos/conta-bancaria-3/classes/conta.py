class ContaBancaria:
    def __init__(self, titular, saldo_inicial, limite):
        self.__saldo = saldo_inicial
        self.limite = limite
        
        self.self = self
        self.titular = titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        print("Não é possível alterar o saldo manualmente!")
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, quantia):
        self.__limite = quantia * -1 if quantia > 0 else quantia
    
    def depositar(self, quantia):
        print(f"Depósito realizado: Saldo: R${self.__saldo}, deposito: R${quantia}")
        self.__saldo += quantia
    
    def sacar(self, quantia):
        if (self.__saldo - quantia > self.limite):
            self.__saldo -= quantia
            print(f"Saque realizado! Saldo: R${self.__saldo}, sacado: R${quantia}")