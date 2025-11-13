from classes.conta import ContaBancaria

conta = ContaBancaria("Victor", 1000, 500)

print(f"Titular: {conta.titular}")
print(f"Saldo inicial: R$ {conta.saldo:.2f}\n")

# Testando o setter do limite
print(f"Limite (definido como 500.0): R$ {conta.limite:.2f}\n")

# Testando depósito
conta.depositar(500.0)
print(f"Saldo após depósito: R$ {conta.saldo:.2f}")

# Testando saque (usando limite)
print("\n--- Tentando sacar R$ 1800.0 (usando o limite) ---")
conta.sacar(1800.0)
print(f"Saldo após saque 1: R$ {conta.saldo:.2f}")

# Testando saque (acima do limite)
print("\n--- Tentando sacar R$ 1000.0 (acima do limite) ---")
conta.sacar(1000.0)
print(f"Saldo final: R$ {conta.saldo:.2f}")

# Teste de proteção (ISSO DEVE FALHAR)
try:
    conta.saldo = 50000.0
except AttributeError as e:
    print(f"\nTeste de proteção (OK): {e}")