class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        
    
    def __str__(self):
        return f"Produto: {self.nome} | Preço: R${self.preco} | Quantidade: {self.estoque} un."
        
    def retirar_do_estoque(self, quantidade):
        if self.estoque >= quantidade:
            self.estoque -= quantidade
            return True
        else: 
            print("Estoque insuficiente!")
            return False
    
    def adicionar_ao_estoque(self, quantidade):
        self.estoque += quantidade