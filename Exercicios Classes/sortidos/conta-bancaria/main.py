from conta_bancaria import ContaBancaria

# --- Bloco de Teste ---
# Crie duas instâncias (objetos) da sua classe
conta_ana = ContaBancaria({
    "titular": "Ana Silva", 
    "saldo": 1500
})
conta_joao = ContaBancaria({
    "titular": "João Costa", 
    "saldo": 3000
})

# Imprima os detalhes iniciais usando o método __str__
print("--- Contas Criadas ---")
print(conta_ana)
print(conta_joao)

# Realize operações na conta da Ana
print("\n--- Operações na Conta de Ana ---")
conta_ana.depositar(500)
conta_ana.sacar(200)
conta_ana.sacar(2000) # Teste de saldo insuficiente
conta_ana.desativar_conta()
conta_ana.sacar(100) # Teste com conta inativa

# Realize operações na conta do João
print("\n--- Operações na Conta de João ---")
conta_joao.sacar(3500) # Teste de saldo insuficiente
conta_joao.depositar(-100) # Teste de depósito inválido

# Imprima os detalhes finais
print("\n--- Saldos Finais ---")
print(conta_ana)
print(conta_joao)