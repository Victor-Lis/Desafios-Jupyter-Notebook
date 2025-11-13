class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_barulho(self):
        return "Subclasses devem implementar este método!"