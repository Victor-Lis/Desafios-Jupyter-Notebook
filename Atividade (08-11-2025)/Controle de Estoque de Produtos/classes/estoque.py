from classes.produto import Produto

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self):
        self.produtos.append(Produto(input("Nome do produto: "), float(input("Preço do produto: ")), int(input("Quantidade: "))))
        print(f"Produto adicionado com sucesso. \n")

    def remover_produto(self):
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        for produto in self.produtos:
            if produto.nome == nome:
                if produto.quantidade >= quantidade:
                    produto.quantidade -= quantidade
                    print(f"Removidos {quantidade} unidades de {nome}.")
                else:
                    print(f"Quantidade insuficiente em estoque para {nome}.")
                break
        else:
            print(f"Produto {nome} não encontrado no estoque.")

    def listar_produtos(self):
        print(f"\n{"-" * 5} ({len(self.produtos)}) Produtos em Estoque {"-" * 5} \n")
        for i, produto in enumerate(self.produtos):
            print(f"{"-" * 5} Produto {i+1} {"-" * 5}")
            print(produto)
            print(f"{'-' * 20} \n")