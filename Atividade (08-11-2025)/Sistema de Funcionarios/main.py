from classes.gerente import Gerente
from classes.vendedor import Vendedor

def main():
    gerente = Gerente("Alice", 8000, 15)  # 15% de bônus
    vendedor = Vendedor("Bob", 3000, 500)  # R$500 de comissão

    print(f"Pagamento do Gerente {gerente.nome}: R${gerente.calcular_pagamento():.2f}")
    print(f"Pagamento do Vendedor {vendedor.nome}: R${vendedor.calcular_pagamento():.2f}")
    
main()