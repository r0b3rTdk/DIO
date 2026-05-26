# 🔒 Encapsulamento em Python

> Controlar quem pode ver e mexer nos dados da sua classe

---

## 1. O Problema que o Encapsulamento Resolve

Imagina que você tem uma conta bancária no código:

```python
class Conta:
    def __init__(self, saldo=0):
        self.saldo = saldo

conta = Conta(100)
conta.saldo = 999999  # ← qualquer um pode fazer isso. Problema!
```

Sem encapsulamento, qualquer parte do código pode modificar o saldo diretamente.
O encapsulamento resolve isso: você **esconde** o dado e **controla** como ele é acessado.

---

## 2. Público vs Privado

### Atributo Público
Qualquer código de fora da classe pode ler e modificar livremente.

```python
self.nome = "João"        # público — sem underscore
self.nro_agencia = "0001" # público
```

### Atributo Privado
Por convenção, começa com `_`. Significa: **"não mexa nisso diretamente"**.

```python
self._saldo = 0   # privado — tem underscore
```

> ⚠️ **Importante:** O `_` é só uma convenção. Python **não bloqueia** de verdade.
> É um aviso para outros devs (e para você mesmo) de que aquele dado não deve ser
> acessado diretamente de fora da classe.

---

## 3. Exemplo Real: Conta Bancária

```python
class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self.nro_agencia = nro_agencia  # público  → pode acessar de fora
        self._saldo = saldo             # privado  → não acesse diretamente

    def depositar(self, valor):         # público → interface controlada
        self._saldo += valor

    def sacar(self, valor):             # público → interface controlada
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo


conta = Conta("0001", 100)
conta.depositar(100)
conta.sacar(50)
print(conta.nro_agencia)       # "0001" — ok, é público
print(conta.mostrar_saldo())   # 150

# conta._saldo = 999999  ← tecnicamente funciona, mas NÃO faça isso
```

**O que aconteceu aqui:**
- `nro_agencia` é público → pode ler de fora, tudo bem
- `_saldo` é privado → só deve ser alterado via `depositar()` e `sacar()`
- Os métodos públicos são a **porta de entrada** controlada para o saldo

---

## 4. `@property` — O Jeito Elegante de Controlar Acesso

Sem `@property`, para ler o saldo você precisa chamar um método:
```python
conta.mostrar_saldo()   # parece método
```

Com `@property`, você acessa como se fosse um atributo normal:
```python
conta.saldo   # parece atributo, mas tem lógica por trás
```

### Como funciona na prática

```python
class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):              # GETTER — chamado quando você faz: foo.x
        return self._x or 0

    @x.setter
    def x(self, value):       # SETTER — chamado quando você faz: foo.x = valor
        self._x += value

    @x.deleter
    def x(self):              # DELETER — chamado quando você faz: del foo.x
        self._x = 0


foo = Foo(10)

print(foo.x)   # → 10       (chamou o getter)

del foo.x
print(foo.x)   # → 0        (deleter zerou, getter retornou 0)

foo.x = 10
print(foo.x)   # → 10       (setter fez 0 += 10)
```

### Os 3 decoradores

| Decorador | Quando é chamado | Para que serve |
|---|---|---|
| `@property` | `foo.x` | Ler o valor (getter) |
| `@x.setter` | `foo.x = valor` | Definir/alterar o valor |
| `@x.deleter` | `del foo.x` | Deletar/resetar o valor |

> 💡 Não precisa implementar os três sempre. O mais comum é usar só
> `@property` + `@x.setter`.

---

## 5. Uso Mais Comum: Calcular na Hora

`@property` é muito usado para atributos **calculados** — aqueles que dependem
de outro dado e não fazem sentido ficar salvos:

```python
class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento  # privado

    @property
    def idade(self):                           # calculado na hora, não salvo
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento


pessoa = Pessoa("Guilherme", 1994)
print(f"Nome: {pessoa.nome}")    # Guilherme
print(f"Idade: {pessoa.idade}")  # 30  ← parece atributo, mas é calculado
```

**Por que não salvar a idade direto?**
Porque a idade muda todo ano. Calcular na hora garante que sempre estará certa.

---

## 6. `__x` — Privado de Verdade

Se quiser dificultar ainda mais o acesso, usa **dois underscores**:

```python
class Cofre:
    def __init__(self, senha):
        self.__senha = senha   # Python embaralha o nome internamente

cofre = Cofre("abc123")
# cofre.__senha         → AttributeError! Não encontra
# cofre._Cofre__senha   → ainda dá pra acessar, mas é feio e intencional
```

| Convenção | Exemplo | Nível de proteção |
|---|---|---|
| Sem underscore | `self.nome` | Público — acesso livre |
| Um underscore | `self._saldo` | Privado por convenção — "não mexa" |
| Dois underscores | `self.__senha` | Privado de verdade — Python embaralha o nome |

---

## 7. Resumo Rápido

```python
class ContaBancaria:
    def __init__(self, agencia, saldo=0):
        self.agencia = agencia    # público
        self._saldo = saldo       # privado (convenção)

    @property
    def saldo(self):              # getter — lê _saldo de forma controlada
        return self._saldo

    @saldo.setter
    def saldo(self, valor):       # setter — valida antes de alterar
        if valor < 0:
            print("Valor inválido!")
            return
        self._saldo = valor

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if valor > self._saldo:
            print("Saldo insuficiente!")
            return
        self._saldo -= valor


conta = ContaBancaria("0001", 500)

print(conta.saldo)    # 500 — getter
conta.saldo = -100    # "Valor inválido!" — setter com validação
conta.depositar(200)
conta.sacar(100)
print(conta.saldo)    # 600
```

**O que o `@property` ganhou aqui:**
- Parece um atributo normal por fora (`conta.saldo`)
- Mas por dentro tem validação (`if valor < 0`)
- Sem `@property`, você teria que chamar `conta.get_saldo()` — menos elegante
