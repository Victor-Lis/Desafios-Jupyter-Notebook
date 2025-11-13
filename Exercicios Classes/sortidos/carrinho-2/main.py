from classes.carrinho import CarrinhoDeCompras
from classes.produto import Produto
# --- Bloco de Teste ---
# 1. Criar os produtos
p1 = Produto("Teclado Mecânico", 350.00)
p2 = Produto("Mouse Gamer", 180.00)
p3 = Produto("Monitor 4K", 1500.00)

# 2. Criar o carrinho e adicionar itens
carrinho = CarrinhoDeCompras()
carrinho.adicionar_produto(p1, 1)
carrinho.adicionar_produto(p2, 2)
carrinho.adicionar_produto(p3, 1)

print("--- Recibo do Carrinho (usando __str__) ---")
print(carrinho)

print("\n--- Informações Adicionais (usando __len__) ---")
print(f"Número de itens diferentes no carrinho: {len(carrinho)}")

carrinho.adicionar_produto(p1, 3)
print("\n--- Recibo Atualizado ---")
print(carrinho)
print(f"Número de itens diferentes (ainda deve ser 3): {len(carrinho)}")