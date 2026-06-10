# 📊 Bibliotecas Essenciais para Análise de Dados

> NumPy, Pandas e Matplotlib — o trio que você vai usar todo dia

---

## 1. A Ideia Geral

Em vez de escrever tudo do zero, você importa bibliotecas que já resolvem problemas complexos.

| Biblioteca | Serve pra |
|---|---|
| `NumPy` | Arrays e operações matemáticas rápidas |
| `Pandas` | Tabelas de dados (como Excel no Python) |
| `Matplotlib` | Gráficos e visualizações |

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

> 💡 O `as np`, `as pd`, `as plt` são apelidos — convenção universal.
> Todo mundo usa assim. Não muda.

---

## 2. NumPy — Arrays e Matemática

### O que é um array?

Array = lista otimizada pra operações matemáticas. Muito mais rápido que lista Python pura.

```python
import numpy as np

array = np.array([1, 2, 3, 4, 5])
print(array)   # [1 2 3 4 5]
```

### Operações em massa — sem loop

```python
numeros = np.array([1, 2, 3, 4])

print(numeros * 2)    # [2 4 6 8]   — multiplica todos de uma vez
print(numeros + 10)   # [11 12 13 14]
print(numeros ** 2)   # [1 4 9 16]
```

Com lista Python normal você precisaria de um loop pra isso. NumPy faz em uma linha.

### Operações estatísticas

```python
notas = np.array([7, 8, 6, 9, 5])

print(np.mean(notas))    # 7.0  — média
print(np.max(notas))     # 9    — máximo
print(np.min(notas))     # 5    — mínimo
print(np.sum(notas))     # 35   — soma
```

---

## 3. Pandas — Tabelas de Dados

### O que é um DataFrame?

DataFrame = tabela com linhas e colunas, como uma planilha Excel dentro do Python.

```python
import pandas as pd

dados = {
    "nome": ["Ana", "Carlos", "Maria"],
    "idade": [25, 30, 28]
}

df = pd.DataFrame(dados)
print(df)
```

```
     nome  idade
0     Ana     25
1  Carlos     30
2   Maria     28
```

### Lendo e salvando CSV

```python
# salvar DataFrame como CSV
df.to_csv("dados.csv", index=False)

# ler um CSV existente
df = pd.read_csv("dados.csv")
```

### Operações básicas

```python
dados = {
    "produto": ["Notebook", "Mouse", "Teclado"],
    "preco": [3500, 120, 200]
}

df = pd.DataFrame(dados)

df["preco"]           # acessa a coluna preco
df["preco"].mean()    # 1273.33 — média
df["preco"].max()     # 3500    — máximo
df["produto"].count() # 3       — quantidade de linhas
```

### `.describe()` — estatísticas de uma vez só

```python
df.describe()
```

```
       preco
count      3.0
mean    1273.3
std     1928.7
min      120.0
25%      160.0
50%      200.0
75%     1850.0
max     3500.0
```

Mostra tudo de uma vez: contagem, média, desvio padrão, mínimo, máximo e percentis.

### Agrupamentos com `groupby`

```python
dados = {
    "produto": ["Notebook", "Mouse", "Mouse", "Teclado"],
    "preco": [3500, 120, 150, 200]
}

df = pd.DataFrame(dados)

df.groupby("produto").mean()
```

```
          preco
produto
Mouse     135.0
Notebook  3500.0
Teclado   200.0
```

`groupby` agrupa as linhas pelo valor de uma coluna e aplica uma função (mean, sum, count...).
Equivalente ao `GROUP BY` do SQL — que você já conhece.

### Filtrando linhas

```python
# produtos com preco > 200
df[df["preco"] > 200]

# produto específico
df[df["produto"] == "Mouse"]
```

---

## 4. Matplotlib — Gráficos

### Gráfico de linha

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title("Evolução de vendas")
plt.xlabel("Mês")
plt.ylabel("Vendas")
plt.show()
```

### Gráfico de barras

```python
produtos = ["Notebook", "Mouse", "Teclado"]
vendas = [15, 50, 30]

plt.bar(produtos, vendas)
plt.title("Vendas por produto")
plt.show()
```

### Gráfico de dispersão (scatter)

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

plt.scatter(x, y)
plt.title("Dispersão")
plt.show()
```

### Gráfico direto do DataFrame (Pandas + Matplotlib juntos)

```python
import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "produto": ["Notebook", "Mouse", "Teclado"],
    "vendas": [15, 50, 30]
}

df = pd.DataFrame(dados)

plt.bar(df["produto"], df["vendas"])
plt.title("Vendas por produto")
plt.show()
```

---

## 5. Fluxo Completo — Da Leitura ao Gráfico

```python
import pandas as pd
import matplotlib.pyplot as plt

# 1. carrega os dados
df = pd.read_csv("vendas.csv")

# 2. explora
print(df.head())        # primeiras 5 linhas
print(df.describe())    # estatísticas gerais

# 3. filtra
df_caro = df[df["preco"] > 500]

# 4. agrupa
por_produto = df.groupby("produto")["vendas"].sum()

# 5. visualiza
plt.bar(por_produto.index, por_produto.values)
plt.title("Total de vendas por produto")
plt.show()
```

---

## 6. Resumo Rápido

| O que fazer | Como fazer |
|---|---|
| Criar array | `np.array([1, 2, 3])` |
| Operação em massa | `array * 2`, `array + 10` |
| Criar tabela | `pd.DataFrame(dicionario)` |
| Ler CSV | `pd.read_csv("arquivo.csv")` |
| Salvar CSV | `df.to_csv("arquivo.csv", index=False)` |
| Acessar coluna | `df["coluna"]` |
| Estatísticas | `df.describe()`, `.mean()`, `.max()` |
| Agrupar | `df.groupby("coluna").mean()` |
| Filtrar linhas | `df[df["coluna"] > valor]` |
| Gráfico de linha | `plt.plot(x, y)` |
| Gráfico de barras | `plt.bar(categorias, valores)` |
| Dispersão | `plt.scatter(x, y)` |

> 📖 Referência Pandas: https://www.w3schools.com/python/pandas/pandas_dataframes.asp
