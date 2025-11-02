class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int):
        self.__nome = None
        self.__preco = None
        self.__quantidade = None

        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, valor: str):
        if not isinstance(valor, str):
            raise TypeError("nome deve ser uma string")
        if valor.strip() == "":
            raise ValueError("nome não pode ser vazio")
        self.__nome = valor

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("preco deve ser numérico")
        valor = float(valor)
        if valor < 0:
            raise ValueError("preco não pode ser negativo")
        self.__preco = valor

    @property
    def quantidade(self) -> int:
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, valor: int):
        if not isinstance(valor, int):
            raise TypeError("quantidade deve ser um inteiro")
        if valor < 0:
            raise ValueError("quantidade não pode ser negativa")
        self.__quantidade = valor