from Contas import ContaCorrente, CartaoCredito

conta_juca = ContaCorrente('Juca', '123.456.789-10', '0123', '11222-3')
print('Correntista: ', conta_juca.nome)
print('CPF: ', conta_juca.cpf)
conta_juca.depositar_dinheiro(10000)
conta_juca.sacar_dinheiro(1000)
conta_juca.consultar_historico_transacoes()
# Criando a conta da mãe do Juca
mae_juca = ContaCorrente("Ana", "222.333.444-55", "5555", '65656-5')
conta_juca.transferir(1200, mae_juca)
conta_juca.consultar_saldo()
mae_juca.consultar_saldo()
conta_juca.consultar_historico_transacoes()
mae_juca.consultar_historico_transacoes()
conta_juca.consultar_saldo()
# help(ContaCorrente)
# Cria um objeto cartao de credito
cartao_juca = CartaoCredito("Juca", conta_juca)
print(cartao_juca)

