# 🐍 Type Hints e For Loops Aninhados

> Por que anotar tipos nas funções e como pensar em for dentro de for

---

## 1. Type Hints — Por que Anotar o Tipo?

Type hint = dica de tipagem. Você avisa ao Python (e a quem lê o código) qual tipo de dado a função espera receber e qual vai retornar.

```python
def media(lista: list) -> float:
    return sum(lista) / len(lista)
```

**Isso não é obrigatório.** O Python não vai dar erro se você passar um tipo errado. Mas serve pra:

- Deixar o código mais legível — quem lê já sabe o que passar
- Ajudar o editor de código a dar sugestões e avisar erros antes de rodar
- Documentar a função sem precisar escrever explicação longa

---

## 2. Quando Usar Cada Tipo na Anotação

### `-> float` — a função retorna um número decimal

```python
def media(lista: list) -> float:
    return sum(lista) / len(lista)

# Retorna: 7.5
```

### `-> list` — a função retorna uma lista

```python
def calcular_notas(testes: list) -> list:
    return [sum(t) for t in testes]

# Retorna: [5, 3, 4]
```

### `-> None` — a função não retorna nada (só faz algo, como `print`)

```python
def exibir_resultado(nome: str, nota: float) -> None:
    print(f"{nome}: {nota}")

# Não retorna nada — só imprime
```

### `-> str` — a função retorna texto

```python
def situacao(media: float) -> str:
    return "Aprovado" if media >= 6 else "Reprovado"
```

### `list[int]`, `list[str]` — lista de tipo específico (Python 3.9+)

```python
def somar_notas(notas: list[int]) -> int:
    return sum(notas)
```

### Resumo

| Anotação | Significa |
|---|---|
| `param: list` | Espera receber uma lista |
| `param: str` | Espera receber texto |
| `param: int` | Espera receber inteiro |
| `param: float` | Espera receber decimal |
| `param: dict` | Espera receber dicionário |
| `param: bool` | Espera receber True ou False |
| `-> float` | A função vai retornar um decimal |
| `-> list` | A função vai retornar uma lista |
| `-> None` | A função não retorna nada |
| `-> str` | A função vai retornar texto |

---

## 3. For Dentro de For — Como Pensar

O `for` aninhado é um `for` dentro de outro `for`. Cada vez que o loop externo avança uma posição, o loop interno roda **completo**.

### Regra de leitura

> **Loop externo** = "para cada coisa grande"
> **Loop interno** = "para cada parte dessa coisa grande"

```python
turma = [
    ['D', 'A', 'B'],   # respostas do aluno 1
    ['C', 'A', 'A'],   # respostas do aluno 2
    ['D', 'B', 'A'],   # respostas do aluno 3
]

for teste in turma:              # para cada aluno
    for alternativa in teste:    # para cada resposta desse aluno
        print(alternativa)
```

O loop externo pega `['D', 'A', 'B']` → o interno percorre `D`, `A`, `B`.
Depois o externo pega `['C', 'A', 'A']` → o interno percorre `C`, `A`, `A`. E assim por diante.

---

## 4. Aplicando no Exercício de Testes

Esse foi o exercício que te deixou perdido. Vamos destrinchar cada `for`:

```python
def verificar_notas(testes_alunos: list) -> list:
    gabarito = ['D', 'A', 'B', 'C', 'A']
    opcoes_validas = ['A', 'B', 'C', 'D']

    try:
        # FOR 1: para cada lista de respostas (cada aluno)
        for teste in testes_alunos:

            # FOR 2: para cada alternativa dentro das respostas desse aluno
            for alternativa in teste:

                # verifica se a alternativa é válida
                if alternativa not in opcoes_validas:
                    raise ValueError(f"A alternativa {alternativa} não é válida")

    except ValueError as e:
        print(f"Erro de Validação: {e}")

    else:
        notas_finais = []

        # FOR 3: de novo para cada aluno (agora pra calcular a nota)
        for teste in testes_alunos:
            nota_aluno = 0

            # FOR 4: zip para comparar resposta do aluno com o gabarito
            for resp_aluno, resp_gabarito in zip(teste, gabarito):
                if resp_aluno == resp_gabarito:
                    nota_aluno += 1

            notas_finais.append(nota_aluno)

        print(f"Notas: {notas_finais}")
        return notas_finais
```

**Por que 4 for loops?** Porque o problema tem duas fases separadas:

**Fase 1 — Validação (FOR 1 + FOR 2):**
```
testes_alunos = [
    ['D', 'A', 'B', 'C', 'A'],   ← FOR 1 pega isso
    ['C', 'A', 'A', 'E', 'A'],   ← FOR 1 pega isso
    ['D', 'B', 'A', 'C', 'A'],   ← FOR 1 pega isso
]

Para cada lista acima, FOR 2 percorre cada letra:
    'D' → válida ✅
    'A' → válida ✅
    'E' → inválida ❌ → raise ValueError → para tudo
```

**Fase 2 — Cálculo (FOR 3 + FOR 4 com zip):**
```
Para cada aluno (FOR 3):
    Para cada par resposta/gabarito (FOR 4 com zip):
        ('D', 'D') → acertou → nota += 1
        ('A', 'A') → acertou → nota += 1
        ('B', 'B') → acertou → nota += 1
    Nota do aluno: 5
```

---

## 5. Como Pensar Antes de Escrever Fors Aninhados

Quando você se deparar com uma lista de listas, pergunte:

```
1. O que é a lista externa?    → cada aluno / cada linha / cada grupo
2. O que é a lista interna?    → cada resposta / cada coluna / cada item
3. O que preciso fazer com cada item interno?  → validar / comparar / somar
```

### Mapeamento mental do exercício:

```
testes_alunos  →  lista de alunos
    teste      →  lista de respostas de UM aluno
    alternativa →  UMA resposta de UM aluno
```

Escrevendo o for assim, de fora pra dentro:

```python
for teste in testes_alunos:       # "para cada aluno"
    for alternativa in teste:     # "para cada resposta desse aluno"
        # faz algo com a alternativa
```

---

## 6. For Aninhado + zip — Comparando Duas Listas ao Mesmo Tempo

No cálculo das notas, o `zip` foi usado dentro do for aninhado pra comparar resposta com gabarito:

```python
gabarito = ['D', 'A', 'B', 'C', 'A']
teste    = ['D', 'A', 'B', 'D', 'A']

for resp_aluno, resp_gabarito in zip(teste, gabarito):
    print(resp_aluno, resp_gabarito)

# D D → acerto
# A A → acerto
# B B → acerto
# D C → errou
# A A → acerto
```

`zip` pareia posição a posição — exatamente o que você precisa pra comparar resposta com gabarito.

---

## 7. Quando Usar For Aninhado vs List Comprehension

```python
# For aninhado — mais legível quando a lógica é complexa
for teste in testes_alunos:
    nota = 0
    for resp, gab in zip(teste, gabarito):
        if resp == gab:
            nota += 1
    notas.append(nota)

# List comprehension — mais conciso quando a lógica é simples
notas = [sum(r == g for r, g in zip(teste, gabarito)) for teste in testes_alunos]
```

**Regra prática:** se o for aninhado tem mais de uma operação ou `if/else` complexo, mantém o for explícito. Se é só uma expressão, list comprehension fica mais limpo.

---

## 8. Resumo

| Conceito | O que é | Quando usar |
|---|---|---|
| `param: list` | Avisa que espera lista | Sempre que a função tem parâmetros com tipo definido |
| `-> float` | Avisa que vai retornar decimal | Quando a função retorna um valor calculado |
| `-> None` | Função não retorna nada | Funções que só fazem `print` ou modificam algo |
| For aninhado | Loop dentro de loop | Quando você tem lista de listas e precisa acessar cada elemento interno |
| `zip` dentro de for | Percorre duas listas juntas | Comparar resposta com gabarito, nome com nota, etc. |
