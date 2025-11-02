from classes.estoque import Estoque

def main():
    estoque = Estoque()

    while True:
        print("\nControle de Estoque")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Listar Produtos")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            estoque.adicionar_produto()

        elif escolha == '2':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            estoque.remover_produto(nome, quantidade)

        elif escolha == '3':
            estoque.listar_produtos()

        elif escolha == '4':
            print("Saindo do sistema de controle de estoque.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
            
main()