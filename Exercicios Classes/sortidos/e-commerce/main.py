from classes.fisico import ProdutoFisico
from classes.digital import ProdutoDigital

teclado = ProdutoFisico("Teclado Mecânico", 350.0, "SKU-TCL-001", 800)
jogo = ProdutoDigital("Jogo Super Aventura", 199.90, "SKU-JOGO-002", "50GB")

print("--- Detalhes do Produto Físico ---")
teclado.exibir_detalhes()

print("\n--- Detalhes do Produto Digital ---")
jogo.exibir_detalhes()