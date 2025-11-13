class CarrinhoDeCompras:
    def __init__(self):
        self.__itens = {}
        
    def adicionar_produto(self, produto, quantidade):
        if produto not in self.__itens:
            self.__itens[produto] = quantidade
        else:
            self.__itens[produto] += quantidade
    
    def __len__(self):
        return len(self.__itens)

    def __str__(self):
        linhas = ["=== Carrinho de Compras ===", ""]
        total = 0
        for produto, quantidade in self.__itens.items():
            nome = None
            preco = None
            if isinstance(produto, str):
                nome = produto
            elif isinstance(produto, (tuple, list)) and len(produto) == 2:
                nome, preco = produto
            else:
                nome = getattr(produto, "nome", None) or getattr(produto, "name", None) or str(produto)
                preco = getattr(produto, "preco", None) or getattr(produto, "price", None)

            if preco is None:
                linhas.append(f"- {nome} ({quantidade} un.)")
            else:
                subtotal = preco * quantidade
                linhas.append(f"- {nome} ({quantidade} un.) - Subtotal: R$ {subtotal:.2f}")
                total+= subtotal
        linhas.append("-" * 25)
        linhas.append(f"Total: R$ {total}")
        return "\n".join(linhas)