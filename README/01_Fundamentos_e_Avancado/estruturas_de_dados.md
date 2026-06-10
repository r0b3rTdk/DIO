# 🗂️ Estruturas de Dados em Python — Guia Completo

> Listas, tuplas, list/dict comprehension, enumerate, zip e count — tudo que importa

---

## 1. Tuplas — Dados que Não Mudam

Tupla = coleção **imutável**. Depois de criada, não dá pra adicionar, alterar ou remover.

```python
cadastro = ("Júlia", 23, "São Paulo", "SP", "Python para DS")
```

### Acessando e desempacotando

```python
print(cadastro[0])    # Júlia
print(cadastro[-1])   # Python para DS

# Desempacotando em variáveis
nome, idade, cidade, estado, turma = cadastro
print(f"{nome} tem {idade} anos, mora em {cidade}-{estado}.")
```

**Quando usar tupla?** Quando os dados não devem mudar — IDs, coordenadas, cadastros fixos, retorno de múltiplos valores de funções.

---

## 2. Listas de Listas

```python
notas = [
    [8.0, 9.0, 10.0],   # João
    [9.0, 7.0, 6.0],    # Maria
    [3.4, 7.0, 7.0],    # José
]
```

### Multi-indexação — acessando elementos dentro de listas

```python
notas[0]       # [8.0, 9.0, 10.0] — lista inteira do João
notas[0][2]    # 10.0              — terceira nota do João
notas[2][0]    # 3.4               — primeira nota do José
```

Lê sempre de **fora pra dentro**: primeiro escolhe a lista, depois o elemento.

---

## 3. `enumerate()` — Índice + Valor no for

`enumerate()` devolve o índice e o valor ao mesmo tempo, sem precisar de contador manual.

```python
# Sem enumerate — jeito antigo e feio
nomes = ["João", "Maria", "José"]
for i in range(len(nomes)):
    print(i, nomes[i])

# Com enumerate — jeito certo
for i, nome in enumerate(nomes):
    print(i, nome)
# 0 João
# 1 Maria
# 2 José
```

### Começando de um índice diferente

```python
for i, nome in enumerate(nomes, start=1):   # começa do 1
    print(i, nome)
# 1 João
# 2 Maria
# 3 José
```

### `enumerate` em list comprehension

```python
nomes = ["João", "Maria", "José"]

# Criar lista de strings "posição: nome"
resultado = [f"{i}: {nome}" for i, nome in enumerate(nomes)]
print(resultado)
# ['0: João', '1: Maria', '2: José']

# Filtrar só os de índice par
pares = [nome for i, nome in enumerate(nomes) if i % 2 == 0]
print(pares)
# ['João', 'José']
```

### `enumerate` + `zip` — iterando duas listas com índice

```python
nomes = ["João", "Maria", "José"]
notas  = [9.0, 7.3, 5.8]

for i, (nome, nota) in enumerate(zip(nomes, notas), start=1):
    print(f"{i}. {nome}: {nota}")
# 1. João: 9.0
# 2. Maria: 7.3
# 3. José: 5.8
```

---

## 4. List Comprehension — Listas em Uma Linha

### Formato básico

```python
[expressao for item in lista]
```

```python
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0]]

def media(lista):
    return sum(lista) / len(lista)

medias = [round(media(n), 1) for n in notas]
print(medias)   # [9.0, 7.3, 5.8]
```

### Com filtro

```python
[expressao for item in lista if condicao]
```

```python
medias = [9.0, 7.3, 5.8, 6.7, 8.5]
aprovados = [m for m in medias if m >= 6]
print(aprovados)   # [9.0, 7.3, 6.7, 8.5]
```

### Com if/else — categorizando

```python
[resultado_if if condicao else resultado_else for item in lista]
```

```python
situacao = ["Aprovado" if m >= 6 else "Reprovado" for m in medias]
print(situacao)
# ['Aprovado', 'Aprovado', 'Reprovado', 'Aprovado', 'Aprovado']
```

### Com `enumerate` no list comprehension

```python
nomes = ["João", "Maria", "José", "Cláudia", "Ana"]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

# Numerar os aprovados com índice original
aprovados = [f"{i+1}. {nomes[i]}: {medias[i]}" for i, m in enumerate(medias) if m >= 6]
print(aprovados)
# ['1. João: 9.0', '2. Maria: 7.3', '4. Cláudia: 6.7', '5. Ana: 8.5']
```

### List comprehension dentro de list comprehension

Útil pra iterar sobre listas de listas — "achatar" ou transformar estruturas aninhadas.

```python
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0]]

# Achatar lista de listas em lista simples
todas_notas = [nota for lista in notas for nota in lista]
print(todas_notas)
# [8.0, 9.0, 10.0, 9.0, 7.0, 6.0, 3.4, 7.0, 7.0]

# Com filtro: só notas acima de 7
notas_altas = [nota for lista in notas for nota in lista if nota > 7]
print(notas_altas)
# [8.0, 9.0, 10.0, 9.0, 7.0]  ← só as maiores que 7
```

---

## 5. Dict Comprehension — Dicionários em Uma Linha

```python
{chave: valor for item in lista}
```

```python
colunas = ["Notas", "Media", "Situação"]
dados   = [notas, medias, situacao]

cadastro = {colunas[i]: dados[i] for i in range(len(colunas))}
```

### Com `enumerate` no dict comprehension

```python
nomes = ["João", "Maria", "José"]

# Dicionário com índice como chave
indice_nomes = {i: nome for i, nome in enumerate(nomes)}
print(indice_nomes)
# {0: 'João', 1: 'Maria', 2: 'José'}

# Invertido: nome como chave, índice como valor
nomes_indice = {nome: i for i, nome in enumerate(nomes)}
print(nomes_indice)
# {'João': 0, 'Maria': 1, 'José': 2}
```

### List comprehension dentro de dict comprehension

Quando cada chave do dicionário precisa de uma lista como valor — muito usado pra agrupar dados.

```python
funcionarios = [
    ("SP", 4500),
    ("RJ", 3800),
    ("SP", 5200),
    ("MG", 4100),
    ("RJ", 4600),
    ("SP", 3900),
]

estados_unicos = list({f[0] for f in funcionarios})   # {'SP', 'RJ', 'MG'}

# Para cada estado, filtra os salários daquele estado
valores_agrupados = {
    estado: [valor[1] for valor in funcionarios if valor[0] == estado]
    for estado in estados_unicos
}

print(valores_agrupados)
# {'SP': [4500, 5200, 3900], 'RJ': [3800, 4600], 'MG': [4100]}
```

**Como ler:** "Para cada `estado` na lista de estados únicos, crie uma chave com esse estado e como valor, uma lista com todos os salários onde o estado bate."

O list comprehension interno `[valor[1] for valor in funcionarios if valor[0] == estado]` roda uma vez pra cada estado — é exatamente isso que faz a estrutura ser tão poderosa.

Você pode ir além e calcular a média de cada grupo:

```python
from statistics import mean

medias_por_estado = {
    estado: round(mean([v[1] for v in funcionarios if v[0] == estado]), 2)
    for estado in estados_unicos
}

print(medias_por_estado)
# {'SP': 4533.33, 'RJ': 4200.0, 'MG': 4100}
```

---

## 6. `count()` — Contando Ocorrências

`count()` conta quantas vezes um valor aparece numa lista ou string.

### Em listas

```python
notas = [7, 8, 9, 7, 10, 7, 8]

print(notas.count(7))    # 3 — o 7 aparece 3 vezes
print(notas.count(8))    # 2
print(notas.count(10))   # 1
```

### Em strings

```python
texto = "banana"
print(texto.count("a"))    # 3
print(texto.count("na"))   # 2 — conta substrings também
```

### Contando em lista de listas ou tuplas

```python
funcionarios = [("SP", 4500), ("RJ", 3800), ("SP", 5200), ("MG", 4100)]

# Pegar só os estados
estados = [f[0] for f in funcionarios]
print(estados.count("SP"))   # 2
print(estados.count("RJ"))   # 1
```

### `count()` + `set()` pra contar todos os valores únicos

```python
situacao = ["Aprovado", "Reprovado", "Aprovado", "Aprovado", "Reprovado"]

contagem = {s: situacao.count(s) for s in set(situacao)}
print(contagem)
# {'Aprovado': 3, 'Reprovado': 2}
```

---

## 7. `zip()` — Revisão Completa

```python
nomes  = ["João", "Maria", "José"]
medias = [9.0, 7.3, 5.8]

# Parear duas listas
pares = list(zip(nomes, medias))
# [('João', 9.0), ('Maria', 7.3), ('José', 5.8)]

# Criar dicionário
dicionario = dict(zip(nomes, medias))
# {'João': 9.0, 'Maria': 7.3, 'José': 5.8}

# Unzip — separar de volta
nomes_sep, medias_sep = zip(*pares)
# ('João', 'Maria', 'José')   /   (9.0, 7.3, 5.8)
```

**Listas de tamanhos diferentes** → para na menor.

---

## 8. Exemplo Completo — Tudo Junto

```python
from random import randint

notas_turma = ['João', 8.0, 9.0, 10.0, 'Maria', 9.0, 7.0, 6.0,
               'José', 3.4, 7.0, 7.0, 'Cláudia', 5.5, 6.6, 8.0, 'Ana', 6.0, 10.0, 9.5]

# 1. Separar nomes e notas
nomes, notas_juntas = [], []
for i, valor in enumerate(notas_turma):       # enumerate: índice + valor
    if i % 4 == 0:
        nomes.append(valor)
    else:
        notas_juntas.append(valor)

# 2. Agrupar notas de 3 em 3
notas = [
    [notas_juntas[i], notas_juntas[i+1], notas_juntas[i+2]]
    for i in range(0, len(notas_juntas), 3)   # list comprehension com range de 3 em 3
]

# 3. Médias
def media(lista):
    return round(sum(lista) / len(lista), 1)

medias = [media(n) for n in notas]

# 4. Situação com if/else no list comprehension
situacao = ["Aprovado" if m >= 6 else "Reprovado" for m in medias]

# 5. IDs (lista de tuplas)
ids = [(nome, nome[0] + str(randint(0, 999))) for nome in nomes]

# 6. Candidatos à bolsa — zip + enumerate + filtro
candidatos = [
    f"{i+1}. {nome}"
    for i, (nome, m) in enumerate(zip(nomes, medias))
    if m >= 8
]
print("Candidatos à bolsa:", candidatos)
# ['1. João', '5. Ana']

# 7. Contagem de situações — count + dict comprehension
contagem = {s: situacao.count(s) for s in set(situacao)}
print("Contagem:", contagem)
# {'Aprovado': 4, 'Reprovado': 1}

# 8. Cadastro final — dict comprehension
colunas = ["Estudante", "Notas", "Media", "Situação"]
dados   = [nomes, notas, medias, situacao]
cadastro = {colunas[i]: dados[i] for i in range(len(colunas))}

for chave, valor in cadastro.items():
    print(f"\n{chave}:")
    for i, v in enumerate(valor):
        print(f"  {i}: {v}")
```

---

## 9. Resumo Rápido

| Técnica | Formato | Serve pra |
|---|---|---|
| List Comprehension | `[expr for x in lista]` | Criar lista transformada |
| Com filtro | `[expr for x in lista if cond]` | Filtrar elementos |
| Com if/else | `[a if cond else b for x in lista]` | Categorizar cada elemento |
| Aninhado | `[expr for lista in listas for x in lista]` | Achatar listas de listas |
| Dict Comprehension | `{k: v for i in lista}` | Criar dicionário |
| Comprehension aninhada | `{k: [x for x in lista if cond] for k in chaves}` | Agrupar dados por categoria |
| `enumerate()` | `for i, v in enumerate(lista)` | Índice + valor no for |
| `zip()` | `list(zip(a, b))` | Parear listas |
| `dict(zip())` | `dict(zip(chaves, valores))` | Dicionário de duas listas |
| Unzip | `a, b = zip(*pares)` | Separar lista de tuplas |
| `count()` | `lista.count(valor)` | Contar ocorrências de um valor |
