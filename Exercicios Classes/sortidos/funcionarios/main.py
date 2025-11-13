from classes.engenheiro import Engenheiro
from classes.gerente import Gerente
from classes.vendedor import Vendedor
from classes.funcionario import Funcionario

func1 = Engenheiro("Ana", 7000.0)
func2 = Gerente("Bruno", 12000.0)
func3 = Vendedor("Carla", 3500.0)
func4 = Funcionario("Genérico", 1000)

equipe = [func1, func2, func3, func4]

print("--- Cálculo de Bônus da Equipe (Polimorfismo) ---")
print("=" * 50)
for f in equipe:
    bonus = f.calcular_bonus()
    print(f"Funcionário: {f.nome} ({f.__class__.__name__})")
    print(f"Salário Base: R$ {f.salario:.2f}")
    print(f"Bônus Calculado: R$ {bonus:.2f}\n")