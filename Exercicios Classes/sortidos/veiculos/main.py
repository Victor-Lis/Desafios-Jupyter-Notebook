from classes.carro import Carro
from classes.moto import Moto
from classes.veiculo import Veiculo

carro = Carro("Toyota", "Corolla", 2023, 177)
moto = Moto("Honda", "CB 500", 2022)

frota = [carro, moto]

print("--- Calculando IPVA da Frota (Polimorfismo) ---")
for veiculo in frota:
    print(f"Veículo: {veiculo.marca} {veiculo.modelo} ({veiculo.__class__.__name__})")
    print(f"IPVA: R$ {veiculo.calcular_ipva():.2f}\n")

try:
    print("Tentando instanciar Veiculo genérico...")
    veiculo_generico = Veiculo("Marca Genérica", "Modelo Genérico", 2020)
except TypeError as e:
    print(f"Teste de abstração (OK): {e}")