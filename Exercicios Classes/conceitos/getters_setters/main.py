from classes.produto import Produto

def main():
    # Criando uma instância de Produto
    produto = Produto("Caneta", 2.50, 100)

    # Exibindo os atributos do produto
    print(f"Produto: {produto.nome}")
    print(f"Preço: R$ {produto.preco:.2f}")
    print(f"Quantidade em estoque: {produto.quantidade}")

    # Modificando os atributos do produto
    produto.preco = 3.00
    produto.quantidade = 150

    # Exibindo os atributos atualizados do produto
    print("\nApós atualização:")
    print(f"Produto: {produto.nome}")
    print(f"Preço: R$ {produto.preco:.2f}")
    print(f"Quantidade em estoque: {produto.quantidade}")
    
if __name__ == "__main__":
    main()