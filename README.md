# Desafios Python - Jupyter

## Descrição
Este repositório contém as soluções para a Lista de Exercícios 1 da disciplina de Programação Orientada a Objetos (POO) do IFSP, desenvolvidas em Python utilizando Jupyter Notebooks.

**Autor:** Victor Lis Bronzo  
**Professor:** César A. S. Lima, Dr.  
**Turma:** B  

## Estrutura do Projeto

O projeto está organizado em 19 exercícios individuais, cada um em seu próprio notebook Jupyter:

- [`exercicio1.ipynb`](Atividade%20%2827-09-2025%29/exercicio1.ipynb) - Conversão de metros para milímetros
- [`exercicio2.ipynb`](Atividade%20%2827-09-2025%29/exercicio2.ipynb) - Conversão de tempo para segundos totais
- [`exercicio3.ipynb`](Atividade%20%2827-09-2025%29/exercicio3.ipynb) - Cálculo de aumento salarial
- [`exercicio4.ipynb`](Atividade%20%2827-09-2025%29/exercicio4.ipynb) - Cálculo de desconto em mercadorias
- [`exercicio5.ipynb`](Atividade%20%2827-09-2025%29/exercicio5.ipynb) - Cálculo de tempo de viagem
- [`exercicio6.ipynb`](Atividade%20%2827-09-2025%29/exercicio6.ipynb) - Cálculo de preço de aluguel de carro
- [`exercicio7.ipynb`](Atividade%20%2827-09-2025%29/exercicio7.ipynb) - Cálculo de redução de vida por cigarro
- [`exercicio8.ipynb`](Atividade%20%2827-09-2025%29/exercicio8.ipynb) - Encontrar maior e menor entre três números
- [`exercicio9.ipynb`](Atividade%20%2827-09-2025%29/exercicio9.ipynb) - Cálculo de aumento salarial com condições
- [`exercicio10.ipynb`](Atividade%20%2827-09-2025%29/exercicio10.ipynb) - Cálculo de preço de passagem por distância
- [`exercicio11.ipynb`](Atividade%20%2827-09-2025%29/exercicio11.ipynb) - Contagem regressiva de foguete
- [`exercicio12.ipynb`](Atividade%20%2827-09-2025%29/exercicio12.ipynb) - Divisão inteira usando apenas soma e subtração
- [`exercicio13.ipynb`](Atividade%20%2827-09-2025%29/exercicio13.ipynb) - Simulação de poupança com juros compostos
- [`exercicio14.ipynb`](Atividade%20%2827-09-2025%29/exercicio14.ipynb) - Cálculo de quitação de dívida
- [`exercicio15.ipynb`](Atividade%20%2827-09-2025%29/exercicio15.ipynb) - Comparação de crescimento populacional
- [`exercicio16.ipynb`](Atividade%20%2827-09-2025%29/exercicio16.ipynb) - Sistema de comissões de vendedores
- [`exercicio17.ipynb`](Atividade%20%2827-09-2025%29/exercicio17.ipynb) - Comparativo de consumo de combustível
- [`exercicio18.ipynb`](Atividade%20%2827-09-2025%29/exercicio18.ipynb) - Análise de vendas de e-commerce
- [`exercicio19.ipynb`](Atividade%20%2827-09-2025%29/exercicio19.ipynb) - Sistema de monitoramento de CO2

## Tecnologias Utilizadas

- **Python 3.13.6**
- **Jupyter Notebook**
- **Bibliotecas:**
  - `random` (para geração de dados aleatórios)
  - Funções built-in do Python (`map`, `zip`, `lambda`, etc.)

## Conceitos Abordados

### Programação Básica
- Entrada e saída de dados (`input()`, `print()`)
- Operações matemáticas básicas
- Formatação de strings (f-strings)
- Conversão de tipos de dados

### Estruturas de Controle
- Condicionais (`if`, `elif`, `else`)
- Operador ternário
- Loops (`for`, `while`)
- List comprehensions

### Estruturas de Dados
- Listas
- Tuplas
- Dicionários
- Funções `zip()` e `map()`

### Funções Avançadas
- Funções lambda
- Funções built-in (`min()`, `max()`, `sum()`, `len()`)
- Funções de ordenação (`sorted()`)

## Como Executar

1. **Pré-requisitos:**
   - Python 3.x instalado
   - Jupyter Notebook ou Jupyter Lab

2. **Instalação:**
   ```bash
   # Instalar Jupyter
   pip install jupyter
   
   # Ou usando conda
   conda install jupyter
   ```

3. **Execução:**
   ```bash
   # Navegar até o diretório do projeto
   cd caminho/para/o/projeto
   
   # Iniciar Jupyter Notebook
   jupyter notebook
   
   # Ou Jupyter Lab
   jupyter lab
   ```

4. **Executar os exercícios:**
   - Abra qualquer arquivo `.ipynb` no Jupyter
   - Execute as células com `Shift + Enter`

## Exemplos de Uso

### Exercício 8 - Maior e Menor Número
```python
# Versão com funções built-in
numeros = list(map(int, input("Escreva 3 números: x,y,z").split(",")))
print("Menor número:", min(numeros))
print("Maior número:", max(numeros))
```

### Exercício 17 - Consumo de Combustível
```python
# Análise de eficiência de carros
lista_carros = ["Fusca", "Gol", "Uno", "Vectra", "Peugeot"]
lista_consumo = [7, 10, 12.5, 9, 14.5]

# Cálculo de consumo para 1000km
for carro, consumo in zip(lista_carros, lista_consumo):
    litros_necessarios = 1000 / consumo
    gasto_total = litros_necessarios * 6.19
    print(f"{carro}: {litros_necessarios:.2f}L - R${gasto_total:.2f}")
```

## Características do Código

- **Código limpo e legível** com nomes de variáveis descritivos
- **Múltiplas abordagens** para alguns problemas (versão simples e otimizada)
- **Uso de recursos avançados** do Python (lambda, list comprehensions)
- **Formatação consistente** de saída com f-strings
- **Tratamento de diferentes cenários** (como no exercício 15)

## Entrega

**Data de entrega:** 27/09/2025 até 23:55h  
**Formato:** Arquivo compactado no Moodle  
**Nome do arquivo:** `Victor_Lis_Bronzo_Exercicio1_BRAPROB_Turma_B`

## Licença

Este projeto foi desenvolvido para fins educacionais como parte do curso de Programação Orientada a Objetos do IFSP.
