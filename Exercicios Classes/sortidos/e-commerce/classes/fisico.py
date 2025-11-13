from classes.produto import Produto

class ProdutoFisico(Produto):
    def __init__(self, nome, preco, sku, peso):
        super().__init__(nome, preco, sku)
        self.peso = peso
        
    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"Peso: {self.peso}g")