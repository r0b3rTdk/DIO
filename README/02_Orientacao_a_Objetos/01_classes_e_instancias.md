# 🗂️ Variáveis de Classe vs Variáveis de Instância

> Onde o atributo mora define quem ele afeta

---

## 1. A Diferença Principal

| | Variável de Instância | Variável de Classe |
|---|---|---|
| Onde fica | Dentro do `__init__`, no `self` | Fora do `__init__`, direto na classe |
| Quem tem | Cada objeto tem a **sua cópia** | **Todos os objetos** compartilham |
| Mudar afeta | Só aquele objeto | Todos os objetos da classe |

---

## 2. Visualizando na Prática

```python
class Estudante:
    escola = "DIO"              # variável de CLASSE — compartilhada por todos

    def __init__(self, nome, matricula):
        self.nome = nome        # variável de INSTÂNCIA — exclusiva de cada objeto
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
```

```python
aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)

print(aluno_1)   # Guilherme - 1 - DIO
print(aluno_2)   # Giovanna  - 2 - DIO
```

Até aqui tudo normal. Agora o ponto chave:

```python
Estudante.escola = "Python"    # muda a variável de CLASSE

aluno_3 = Estudante("Chappie", 3)

print(aluno_1)   # Guilherme - 1 - Python  ← mudou! nem foi criado agora
print(aluno_2)   # Giovanna  - 2 - Python  ← mudou também
print(aluno_3)   # Chappie   - 3 - Python
```

**Todos mudaram** — inclusive os que já existiam antes da mudança.
Isso porque `escola` é uma variável de classe — todos apontam pro mesmo lugar.

---

## 3. E se mudar via objeto?

Aqui mora a maior armadilha do assunto:

```python
aluno_1.escola = "Outra escola"   # muda via OBJETO, não via Classe

print(aluno_1)   # Guilherme - 1 - Outra escola  ← só o aluno_1 mudou
print(aluno_2)   # Giovanna  - 2 - Python         ← aluno_2 não mudou
print(aluno_3)   # Chappie   - 3 - Python         ← aluno_3 não mudou
```

Quando você faz `aluno_1.escola = "..."`, o Python **não altera a variável de classe**.
Ele cria uma **cópia exclusiva** do atributo só no `aluno_1` — e a partir desse momento
o `aluno_1` fica "desconectado" da variável de classe.

```
Antes:   aluno_1 ──┐
         aluno_2 ──┼──► Estudante.escola = "Python"
         aluno_3 ──┘

Depois:  aluno_1 ──────► "Outra escola"  (cópia própria)
         aluno_2 ──┬──► Estudante.escola = "Python"
         aluno_3 ──┘
```

---

## 4. Resumo das Regras

```python
# muda pra TODOS (certo pra variável de classe)
Estudante.escola = "novo valor"

# cria cópia SÓ naquele objeto (desconecta da classe)
aluno_1.escola = "novo valor"

# lê o valor (busca no objeto primeiro, depois na classe)
print(aluno_1.escola)
```

---

## 5. Quando usar variável de classe?

- Valor **igual para todos** os objetos (nome da escola, empresa, configuração padrão)
- **Contador** de quantas instâncias foram criadas

```python
class Produto:
    total = 0   # conta quantos produtos existem

    def __init__(self, nome):
        self.nome = nome
        Produto.total += 1   # incrementa a classe, não o objeto

p1 = Produto("Notebook")
p2 = Produto("Mouse")
p3 = Produto("Teclado")

print(Produto.total)   # 3
```

---

## 6. Dica Importante

> ⚠️ Nunca mude uma variável de classe via objeto (`objeto.atributo = ...`)
> a menos que queira criar uma cópia exclusiva só naquele objeto.
> Pra mudar pra todos, sempre use `Classe.atributo = ...`.
