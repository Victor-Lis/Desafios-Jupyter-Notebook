class Produto:
    def __init__(self, nome, preco, sku):
        self.nome = nome
        self.preco = preco
        self.sku = sku
        
    def exibir_detalhes(self):
        print(f"Nome: {self.nome}")
        print(f"Preço: {self.preco}")
        print(f"SKU: {self.sku}")
        