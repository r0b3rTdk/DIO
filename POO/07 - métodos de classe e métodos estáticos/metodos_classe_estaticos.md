# ⚙️ Métodos de Classe e Métodos Estáticos

> Dois tipos especiais de método — cada um com um propósito claro

---

## 1. Os 3 Tipos de Método em Python

```python
class Exemplo:

    def metodo_normal(self):      # recebe self  → acessa o OBJETO
        pass

    @classmethod
    def metodo_classe(cls):       # recebe cls   → acessa a CLASSE
        pass

    @staticmethod
    def metodo_estatico():        # não recebe nada → função isolada
        pass
```

---

## 2. Método de Classe (`@classmethod`)

Recebe `cls` (a própria classe) como primeiro parâmetro.
Com isso, pode **acessar e modificar atributos da classe**.

**Uso mais comum: método fábrica** — uma forma alternativa de criar um objeto.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)   # cls() = Pessoa() — cria o objeto


# jeito normal
p1 = Pessoa("Ana", 25)

# jeito alternativo via método fábrica
p2 = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")

print(p2.nome, p2.idade)   # Guilherme 28
```

**Por que `cls` em vez de `Pessoa()` direto?**

Porque se outra classe herdar `Pessoa`, o `cls` vai criar o tipo certo — não sempre `Pessoa`.

```python
class Aluno(Pessoa):
    pass

a = Aluno.criar_de_data_nascimento(2000, 1, 1, "João")
print(type(a))   # <class 'Aluno'>  ← criou Aluno, não Pessoa
# se usasse Pessoa() direto, sempre criaria Pessoa — errado
```

---

## 3. Método Estático (`@staticmethod`)

Não recebe `self` nem `cls`. É uma função normal que mora dentro da classe
porque faz sentido estar lá — mas **não depende do objeto nem da classe**.

**Uso mais comum: funções utilitárias** relacionadas à classe.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @staticmethod
    def e_maior_idade(idade):     # não precisa de self nem cls
        return idade >= 18


print(Pessoa.e_maior_idade(18))   # True
print(Pessoa.e_maior_idade(8))    # False

# pode chamar sem criar objeto nenhum
```

---

## 4. Exemplo Completo — Tudo Junto

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)   # método fábrica

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18        # utilitária


p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p.nome, p.idade)           # Guilherme 28

print(Pessoa.e_maior_idade(18))  # True
print(Pessoa.e_maior_idade(8))   # False
```

---

## 5. Comparativo Final

| | Normal | `@classmethod` | `@staticmethod` |
|---|---|---|---|
| Primeiro parâmetro | `self` (objeto) | `cls` (classe) | nenhum |
| Acessa atributos do objeto | ✅ | ❌ | ❌ |
| Acessa atributos da classe | ✅ | ✅ | ❌ |
| Precisa de objeto criado pra chamar | ✅ | ❌ | ❌ |
| Uso típico | Comportamento do objeto | Método fábrica | Função utilitária |

---

## 6. Dica Importante

> Se o método **não usa `self` nem precisa do objeto**, é candidato a `@staticmethod`.
> Se o método **precisa criar um objeto da própria classe de forma alternativa**, é candidato a `@classmethod`.
> Se precisar dos dados do objeto, é método normal.
