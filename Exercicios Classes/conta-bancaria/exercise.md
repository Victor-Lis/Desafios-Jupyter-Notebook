# Exercício: Modelagem de uma Conta Bancária

Você foi encarregado de desenvolver uma classe `ContaBancaria` para simular as operações básicas de uma conta de banco. O objetivo é criar um **molde** (a classe) que possa ser usado para criar múltiplos objetos de conta, cada um com seus próprios dados e capaz de realizar suas próprias operações.

---

## Sua Tarefa

Implemente uma classe chamada `ContaBancaria` que atenda aos seguintes requisitos:

### 1. **Atributos (Dados da Classe)**

A classe deve ser inicializada com os seguintes atributos no método `__init__`:

- **titular**: O nome do titular da conta (string).
- **saldo_inicial**: O saldo com que a conta é aberta (float ou int).
- **numero_conta**: Um número único que identifica a conta (int).
- **ativa**: Indica se a conta está operacional (`True` por padrão).

---

### 2. **Métodos (Ações da Classe)**

#### `depositar(self, valor)`
- Recebe um valor a ser adicionado ao saldo.
- Verifica se o valor do depósito é positivo.
    - Se for, adiciona ao saldo e imprime uma mensagem de sucesso.
    - Se não, imprime uma mensagem de erro.

#### `sacar(self, valor)`
- Recebe um valor a ser subtraído do saldo.
- Verifica as seguintes condições:
    - A conta está ativa?
    - O valor do saque é positivo?
    - O saldo é suficiente para cobrir o saque?
- Se todas as condições forem atendidas:
    - Subtrai o valor do saldo e imprime uma mensagem de sucesso.
- Se qualquer condição falhar:
    - Imprime uma mensagem de erro apropriada:
        - "Conta inativa."
        - "Valor de saque inválido."
        - "Saldo insuficiente."

#### `desativar_conta(self)`
- Altera o atributo `ativa` para `False`.
- Imprime uma mensagem informando que a conta foi desativada.

#### `ativar_conta(self)`
- Altera o atributo `ativa` para `True`.
- Imprime uma mensagem informando que a conta foi reativada.

---

### 3. **Método Especial `__str__` (Representação em String)**

Implemente o método `__str__` para que, ao usar `print()` em um objeto da classe, ele retorne uma string formatada com um resumo da conta, como:

```
Conta Nº: [numero_conta]
Titular: [titular]
Saldo: R$ [saldo]
Status: [Ativa/Inativa]
```

---

> **Dica:** Utilize boas práticas de programação e comentários para tornar seu código mais legível.