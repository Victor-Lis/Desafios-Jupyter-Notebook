from random import randrange

class ContaBancaria:
    def __init__(self, dados_conta):
        self.titular = dados_conta.get('titular')
        self.saldo = dados_conta.get('saldo', 0)
        self.numero_conta = int(f"{randrange(100, 1000)}{randrange(100, 1000)}{randrange(100, 1000)}")
        self.ativa = True

    def __str__(self):
        stringValue = f"\nConta Nº: {self.numero_conta}\n"
        stringValue += f"Titular: {self.titular}\n"
        stringValue += f"Saldo: R$ {self.saldo}\n"
        stringValue += f"Status: {"Ativa" if self.ativa else "Inativa"}\n"
        return stringValue

    def depositar(self, valor):
        if valor > 0: 
            print(f"[Depósito] Saldo Anterior: R${self.saldo}")
            self.saldo += valor 
            print(f"[Depósito] Saldo Atual: R${self.saldo} (+R${valor})\n")
        else: 
            print("[Depósito] Valor deve ser positivo!")

    def sacar(self, valor):
        if self.saldo >= valor and self.ativa: 
            print(f"[Saque] Saldo Anterior: R${self.saldo}")
            self.saldo -= valor 
            print(f"[Saque] Saldo Atual: R${self.saldo} (-R${valor})\n")
        elif not self.ativa: 
            print("[Saque] Conta inativa.")
        elif valor <= 0: 
            print("[Saque] Valor de saque inválido.")
        else:
            print("[Saque] Saldo insuficiente.")

    def desativar_conta(self):
        self.ativa = False
        print("[Conta] Desativada!")
    
    def ativar_conta(self):
        self.ativa = True
        print("[Conta] Reativada!")