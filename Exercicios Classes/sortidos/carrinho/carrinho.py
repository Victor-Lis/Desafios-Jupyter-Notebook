class CarrinhoDeCompras:
    def __init__(self):
        self.itens = {}
        
    def adicionar_item(self, produto, quantidade):
        if produto.retirar_do_estoque(quantidade):
            self.itens[produto] = quantidade
            print("Produto adicionado com sucesso!")
            
    def remover_item(self, produto):
        if produto in self.itens.keys():
            produto.adicionar_ao_estoque(self.itens[produto])
            del self.itens[produto]
            print(f"Produto {produto.nome} removido com sucesso!")
        else:
            print("Produto não está no carrinho!")
            
    def calcular_total(self):
        total = 0
        for produto, quantidade in self.itens.items():
            total += produto.preco * quantidade
        return total
    
    def __str__(self):
        saida = "Itens no carrinho:\n"
        for produto, quantidade in self.itens.items():
            subtotal = produto.preco * quantidade
            saida += f"- {produto.nome}: {quantidade} x R${produto.preco:.2f} = R${subtotal:.2f}\n"
        saida += f"Total da compra: R${self.calcular_total():.2f}"
        return saida