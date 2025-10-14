# Manipular datas e horas
from datetime import datetime
# Manipular Fuso Horário
import pytz
from random import randint

class ContaCorrente:
    """
    Cria um objeto ContaCorrente para gerenciar as contas
    dos clientes:
    nome (str): nome do cliente
    CPF (str): CPF do cliente, deve ser inserido com
    pontos e traços(xxx.xxx.xxx-xx)
    agencia (str): número da agência
    num_conta (str): número da conta do cliente
    saldo (float): saldo disponível na conta do cliente
    limite (float): limite do cheque especial
    transações (list): Extrato bancário
    """

    @staticmethod
    def data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')
    
    # Construtor da Classe ContaCorrente
    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.__saldo = 0
        self.agencia = agencia
        self.num_conta = num_conta
        self.limite = None
        self.transacoes = []
        self.cartoes = []
        pass

    def consultar_saldo(self):
        print(f'O saldo atual de {self.nome} = R$ {self.__saldo:,.2f}')
        pass

    def depositar_dinheiro(self, valor):
        self.__saldo += valor
        self.transacoes.append((valor, self.__saldo, ContaCorrente.data_hora()))
        pass

    def sacar_dinheiro(self, valor):
        if self.__saldo - valor < self.limite_conta():
            print('Você não possui saldo suficiente para sacar este valor!')
            self.consultar___saldo()
        else:
            self.__saldo -= valor
            self.transacoes.append((valor, self.__saldo, ContaCorrente.data_hora()))
        pass

    def limite_conta(self):
        self.limite = -1000
        return self.limite
    
    def consultar_historico_transacoes(self):
        print('\n-- Histórico Transações --')
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        # Abater o valor a ser transferido
        self.__saldo -= valor
        # Incluindo a transferência de valores entre 
        # contas, na lista de transações da conta de origem
        self.transacoes.append((-valor, self.__saldo, ContaCorrente.data_hora()))
        # Incluindo o valor a ser transferido para conta destino
        # OBS: valor e conta_destino não contém o parâmetro self
        # porque são externos.
        conta_destino.__saldo += valor
        # # Incluindo o valor a ser transferido para conta destino
        conta_destino.transacoes.append((valor, conta_destino.__saldo, ContaCorrente.data_hora()))


class CartaoCredito:
    @staticmethod
    def data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR
    
    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000,9999999999999999)
        self.titular = conta_corrente.nome
        self.validade = '{}/{}'.format(CartaoCredito.data_hora().month, CartaoCredito.data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(0, 9))
        self.limite = 1000
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)
        pass
    
    def __str__(self):
        return f'\n-- Cartão de Crédito --\nNúmero: {self.numero}, Titular: {self.titular}, Validade: {self.validade}, Limite: R$ {self.limite:,.2f}'