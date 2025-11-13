from classes.produto import Produto

class ProdutoDigital(Produto):
    def __init__(self, nome, preco, sku, tamanho_arquivo):
        super().__init__(nome, preco, sku)
        self.tamanho_arquivo = tamanho_arquivo
        
    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"Tamanho do Arquivo: {self.tamanho_arquivo}")