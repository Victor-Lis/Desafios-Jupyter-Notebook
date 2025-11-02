class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int):
        self.__nome = None
        self.__preco = None
        self.__quantidade = None

        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


    # definindo como um "getter"
    @property
    def nome(self) -> str:
        return self.__nome

    # definindo como um "setter" do atributo nome
    @nome.setter
    def nome(self, valor: str):
        if not isinstance(valor, str):
            raise TypeError("nome deve ser uma string")
        if valor.strip() == "":
            raise ValueError("nome não pode ser vazio")
        self.__nome = valor

    # definindo como um "getter"
    @property
    def preco(self) -> float:
        return self.__preco

    # definindo como um "setter" do atributo preco
    @preco.setter
    def preco(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("preco deve ser numérico")
        valor = float(valor)
        if valor < 0:
            raise ValueError("preco não pode ser negativo")
        self.__preco = valor

    # definindo como um "getter"
    @property
    def quantidade(self) -> int:
        return self.__quantidade

    # definindo como um "setter" do atributo quantidade
    @quantidade.setter
    def quantidade(self, valor: int):
        if not isinstance(valor, int):
            raise TypeError("quantidade deve ser um inteiro")
        if valor < 0:
            raise ValueError("quantidade não pode ser negativa")
        self.__quantidade = valor

    # Optei por usar o próprio __str__ como o "método para exibir detalhes do produto"
    def __str__(self):
        return (
            f"Produto: {self.nome}\n"
            f"Preço: R$ {self.preco:,.2f}\n"
            f"Quantidade: {self.quantidade} {'un' if self.quantidade == 1 else 'un(s)'}\n"
            f"Valor total: R$ {self.preco * self.quantidade:,.2f}"
        )