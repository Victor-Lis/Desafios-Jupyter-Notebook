from carrinho import CarrinhoDeCompras
from produto import Produto

# --- Bloco de Criação dos Produtos ---
produto1 = Produto("Teclado Mecânico", 350.00, 10)
produto2 = Produto("Mouse Gamer", 150.00, 20)
produto3 = Produto("Monitor 24 polegadas", 950.00, 5)

print("--- Vendo Estoque Inicial ---")
print(produto1)
print(produto2)
print(f"{produto3}\n")

# --- Bloco de Teste ---
carrinho = CarrinhoDeCompras()

# Adicionando itens
print("--- Adicionando Itens ---")
carrinho.adicionar_item(produto1, 2)
carrinho.adicionar_item(produto2, 3)
carrinho.adicionar_item(produto3, 6) # Teste de estoque insuficiente

# Exibindo o carrinho
print("\n--- Carrinho Atual ---")
print(carrinho)

# Removendo um item
print("\n--- Removendo Item ---")
carrinho.remover_item(produto2)

# Exibindo o carrinho final
print("\n--- Carrinho Final ---")
print(carrinho)

# Verificando o estoque restante dos produtos
print("\n--- Estoque Atualizado ---")
print(f"Estoque do {produto1.nome}: {produto1.estoque}")
print(f"Estoque do {produto2.nome}: {produto2.estoque}")