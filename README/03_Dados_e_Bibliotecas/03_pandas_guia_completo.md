# 🐼 Pandas — Guia Completo de Análise de Dados

> Carregar, explorar, limpar, filtrar, agrupar e salvar dados com Pandas

---

## 1. Carregando Dados

```python
import pandas as pd

# CSV com separador padrão (vírgula)
dados = pd.read_csv('arquivo.csv')

# CSV com separador diferente (ponto e vírgula)
dados = pd.read_csv('arquivo.csv', sep=';')

# Diretamente de uma URL
url = 'https://raw.githubusercontent.com/.../aluguel.csv'
dados = pd.read_csv(url, sep=';')
```

---

## 2. Explorando o DataFrame

```python
dados.head()       # 5 primeiras linhas
dados.head(10)     # N primeiras linhas
dados.tail()       # 5 últimas linhas
dados.tail(3)      # N últimas linhas

dados.shape        # (linhas, colunas) → (9800, 9)
dados.shape[0]     # só as linhas
dados.shape[1]     # só as colunas

dados.columns      # nome de todas as colunas
dados.dtypes       # tipo de dado de cada coluna
dados.info()       # resumo: nomes, tipos, não-nulos
dados.describe()   # média, desvio padrão, mín, máx, percentis
```

---

## 3. Acessando Colunas

```python
# Uma coluna → retorna Series
dados['Valor']
dados.Tipo          # funciona se o nome não tiver espaço

# Múltiplas colunas → retorna DataFrame
dados[['Quartos', 'Valor']]
```

> 💡 `dados['Valor']` = **Series** (uma coluna).
> `dados[['Valor']]` = **DataFrame** (tabela com uma coluna).
> A diferença importa ao encadear métodos como `.sort_values()`.

---

## 4. Valores Únicos e Contagem

```python
# Lista dos valores únicos
dados['Tipo'].unique()
# ['Quitinete', 'Casa', 'Apartamento', ...]

# QUANTIDADE de valores únicos (só o número)
dados['Tipo'].nunique()
# 22

# Contagem de cada valor
dados['Tipo'].value_counts()
# Apartamento    19532

# Contagem em percentual
dados['Tipo'].value_counts(normalize=True)
# Apartamento    0.845139
```

> `unique()` → **quais** são | `nunique()` → **quantos** são

---

## 5. Valores Ausentes (NaN)

### Identificando

```python
# DataFrame booleano — True onde tem NaN
df.isnull()

# Quantidade de NaN por coluna
df.isnull().sum()
# Valor          0
# Condominio   745
# IPTU        5472

# Percentual de NaN por coluna
df.isnull().sum() / len(df) * 100
```

### Tratando

```python
# Opção 1 — Preencher com um valor fixo
df = df.fillna(0)               # preenche todos os NaN com 0
df['Valor'] = df['Valor'].fillna(df['Valor'].mean())  # preenche com a média

# Opção 2 — Preencher com o valor anterior/posterior
df = df.fillna(method='ffill')  # usa o valor da linha anterior
df = df.fillna(method='bfill')  # usa o valor da próxima linha

# Opção 3 — Remover linhas com NaN
df = df.dropna()                # remove qualquer linha com NaN
df = df.dropna(subset=['Valor'])  # remove só onde 'Valor' é NaN

# Opção 4 — Interpolar (calcula a partir dos vizinhos)
df = df.interpolate()
```

**Quando usar cada um:**

| Situação | Abordagem |
|---|---|
| Dado não foi registrado (faltou na aula) | `fillna(0)` |
| Série temporal com poucos NaN | `interpolate()` |
| Dado depende do contexto anterior | `fillna(method='ffill')` |
| Coluna muito incompleta (>50% NaN) | `dropna(subset=['coluna'])` |
| NaN vai estragar o modelo de ML | `fillna(media)` ou `dropna()` |

---

## 6. Removendo Linhas e Colunas com `drop()`

`drop()` é a borracha do Pandas. Remove linhas ou colunas do DataFrame.

### O parâmetro `axis`

- `axis=0` → remove **linhas** (horizontal)
- `axis=1` → remove **colunas** (vertical)

```python
# Removendo colunas
df.drop('Tipo', axis=1, inplace=True)
df.drop(['Tipo', 'Bairro'], axis=1, inplace=True)

# Jeito moderno (sem precisar do axis)
df.drop(columns=['Tipo'])
df.drop(columns=['Tipo', 'Bairro'])

# Removendo linhas pelo índice
df.drop([2, 5], axis=0, inplace=True)
df.drop(index=[2, 5])

# Removendo linhas por condição — primeiro pega os índices, depois dropa
indices = df.query('Valor == 0').index
df.drop(indices, axis=0, inplace=True)
```

### O `inplace=True`

Sem `inplace`, o Pandas retorna uma prévia sem modificar o original:

```python
# ❌ Não salva — só mostra
df.drop(columns=['Tipo'])

# ✅ Modifica o df original
df.drop(columns=['Tipo'], inplace=True)

# ✅ Também funciona — sobrescreve a variável
df = df.drop(columns=['Tipo'])
```

---

## 7. Filtrando Dados

### Com `query()` — jeito simples

```python
df.query('Tipo == "Apartamento"')
df.query('Valor > 2000')
df.query('Quartos >= 2 and Valor < 3000 and Area > 70')

# Com variável Python — usa @
imoveis_comerciais = ['Conjunto Comercial/Sala', 'Prédio Inteiro']
df.query('@imoveis_comerciais not in Tipo')
```

### Com seleção booleana — jeito manual

```python
# Cria uma seleção (série de True/False)
selecao1 = df['Quartos'] == 1
selecao2 = df['Valor'] < 1200

# Aplica a seleção no DataFrame
df[selecao1]

# Combina seleções
selecao_final = (selecao1) & (selecao2)   # & = AND (e)
df[selecao_final]

# Operadores disponíveis
# &  → AND (e)
# |  → OR (ou)
# ~  → NOT (não)

# Inline (sem variável intermediária)
df[(df['Quartos'] == 1) & (df['Valor'] < 1200)]
```

> `query()` é mais legível. A seleção booleana é mais flexível pra condições complexas.

---

## 8. Substituindo Valores com `replace()`

`replace()` é o Ctrl+H do Pandas — localiza e substitui valores.

```python
# Substituir um valor
df['Notas'] = df['Notas'].replace(7.0, 8.0)

# Substituir vários valores (listas)
df['Nome'] = df['Nome'].replace(['Alice', 'Beto'], ['Alicia', 'Roberto'])

# Substituir com dicionário — jeito mais profissional
df['Bairro'] = df['Bairro'].replace({
    'Centro': 'Região Central',
    'Copacabana': 'Zona Sul',
    'Barra da Tijuca': 'Zona Oeste'
})
```

> ⚠️ `replace()` só substitui o valor **exato** — não substitui partes de texto.
> Para substituir partes de strings, use `.str.replace()`.

---

## 9. Agrupamento com `groupby()`

```python
# Média por tipo
dados.groupby('Tipo')['Valor'].mean()

# Média com ordenação
dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')

# Múltiplas colunas de agrupamento
dados.groupby(['Tipo', 'Quartos'])[['Valor']].mean()

# Outras funções
dados.groupby('Tipo')['Valor'].sum()
dados.groupby('Tipo')['Valor'].count()
dados.groupby('Tipo')['Valor'].max()
dados.groupby('Tipo')['Valor'].min()
```

---

## 10. Convertendo e Renomeando

```python
# Series → DataFrame
df['Tipo'].value_counts(normalize=True).to_frame()

# Renomear colunas
df.rename(columns={'Tipo': 'Percentuais'}, inplace=True)
df.rename(columns={'Tipo': 'Percentuais', 'Valor': 'Preco'}, inplace=True)
```

> ⚠️ Na versão nova do Pandas, a coluna do `value_counts(normalize=True)`
> é chamada `proportion`. Em versões antigas, fica com o nome da coluna original.

---

## 11. Salvando Dados

```python
# Salvar CSV — problema: gera coluna "Unnamed: 0" extra
df.to_csv('dados.csv')

# ✅ Salvar sem o índice extra
df.to_csv('dados.csv', index=False)

# ✅ Salvar com separador específico
df.to_csv('dados.csv', index=False, sep=';')

# Outros formatos
df.to_excel('dados.xlsx', index=False)
df.to_json('dados.json')
```

**Por que `index=False`?** Sem ele, o Pandas salva os índices do DataFrame como uma coluna extra chamada `Unnamed: 0`, que não tem utilidade.

---

## 12. Gráficos com Pandas + Matplotlib

```python
import matplotlib.pyplot as plt

df_media = dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')
df_media.plot(kind='barh', figsize=(14, 10), color='purple')
plt.show()

df_percentual.plot(
    kind='bar',
    figsize=(14, 10),
    color='green',
    edgecolor='black',
    xlabel='Tipos',
    ylabel='Percentual'
)
plt.show()
```

| `kind=` | Gráfico |
|---|---|
| `'bar'` | Barras verticais |
| `'barh'` | Barras horizontais |
| `'line'` | Linha |
| `'pie'` | Pizza |
| `'scatter'` | Dispersão |
| `'hist'` | Histograma |

---

## 13. Fluxo Completo de Limpeza e Análise

```python
import pandas as pd
import matplotlib.pyplot as plt

# 1. Carrega
dados = pd.read_csv(url, sep=';')

# 2. Explora
print(dados.shape)
print(dados.dtypes)
print(dados.isnull().sum())

# 3. Remove categorias indesejadas
imoveis_comerciais = ['Conjunto Comercial/Sala', 'Prédio Inteiro']
df = dados.query('@imoveis_comerciais not in Tipo')

# 4. Trata NaN
df = df.fillna(0)

# 5. Remove linhas inconsistentes
indices = df.query('Valor == 0 | Condominio == 0').index
df.drop(indices, axis=0, inplace=True)

# 6. Remove coluna desnecessária
df = df.query('Tipo == "Apartamento"')
df.drop(columns=['Tipo'], inplace=True)

# 7. Aplica filtros
df_1quarto = df.query('Quartos == 1 and Valor < 1200')
df_grande  = df.query('Quartos >= 2 and Valor < 3000 and Area > 70')

# 8. Analisa
df_media = df.groupby('Bairro')[['Valor']].mean().sort_values('Valor')

# 9. Plota
df_media.tail(10).plot(kind='barh', figsize=(12, 6), color='steelblue')
plt.title('Top 10 bairros mais caros')
plt.show()

# 10. Salva
df.to_csv('dados_limpos.csv', index=False, sep=';')
```

---

## 14. Criando Colunas Numéricas

Você pode criar uma nova coluna fazendo operações entre colunas existentes:

```python
# Soma de duas colunas linha por linha
dados['Valor_por_mes'] = dados['Valor'] + dados['Condominio']

# Cálculo mais complexo
dados['Valor_por_ano'] = dados['Valor_por_mes'] * 12 + dados['IPTU']
```

> ⚠️ Se alguma coluna tiver NaN, o resultado também será NaN.
> Trate os nulos antes: `dados.fillna(0, inplace=True)`

---

## 15. Criando Colunas Categóricas (Texto)

### Concatenando strings

```python
# Concatenação simples — fica grudado
dados['Descricao'] = dados['Tipo'] + dados['Bairro']
# "QuitineteCopacabana"

# Com separador
dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro']
# "Quitinete em Copacabana"
```

### Concatenando string com número — precisa de `astype(str)`

```python
# ❌ TypeError — não dá pra somar string com int
dados['Descricao'] = dados['Tipo'] + ' com ' + dados['Quartos'] + ' quarto(s)'

# ✅ Converte a coluna numérica para string antes
dados['Descricao'] = (
    dados['Tipo'] + ' em ' + dados['Bairro'] +
    ' com ' + dados['Quartos'].astype(str) + ' quarto(s)' +
    ' e ' + dados['Vagas'].astype(str) + ' vaga(s) de garagem.'
)
# "Quitinete em Copacabana com 1 quarto(s) e 0 vaga(s) de garagem."
```

### Com `apply()` + `lambda` — coluna condicional

```python
# Cria coluna binária baseada em outra coluna
dados['Possui_suite'] = dados['Suites'].apply(lambda x: "Sim" if x > 0 else "Não")
```

Lê assim: para cada valor `x` na coluna `Suites`, se `x > 0` → `"Sim"`, senão → `"Não"`.

### Com `assign()` — alternativa ao método direto

```python
# Cria a coluna e retorna um novo DataFrame (não modifica o original)
dados = dados.assign(Valor_por_mes=dados['Valor'] + dados['Condominio'])

# Encadeando várias criações de uma vez
dados = dados.assign(
    Valor_por_mes=dados['Valor'] + dados['Condominio'],
    Possui_suite=dados['Suites'].apply(lambda x: "Sim" if x > 0 else "Não")
)
```

### Convertendo tipo de dado com `astype()`

```python
dados['Quartos'].astype(str)     # int → string
dados['Valor'].astype(int)       # float → int
dados['Aprovado'].astype(bool)   # 0/1 → False/True
```

---

## 16. Resumo Rápido

| O que fazer | Como fazer |
|---|---|
| Carregar CSV | `pd.read_csv('arquivo.csv', sep=';')` |
| Primeiras/últimas linhas | `df.head(n)` / `df.tail(n)` |
| Tamanho | `df.shape` |
| Tipos das colunas | `df.dtypes` / `df.info()` |
| Estatísticas | `df.describe()` |
| Valores únicos (lista) | `df['col'].unique()` |
| Qtd de valores únicos | `df['col'].nunique()` |
| Contagem de valores | `df['col'].value_counts()` |
| Contagem em % | `df['col'].value_counts(normalize=True)` |
| NaN por coluna | `df.isnull().sum()` |
| Preencher NaN | `df.fillna(valor)` |
| Remover linhas com NaN | `df.dropna()` |
| Filtrar linhas | `df.query('condicao')` |
| Filtro booleano | `df[(df['col'] == val) & (df['col2'] > val2)]` |
| Remover coluna | `df.drop(columns=['col'])` |
| Remover linhas | `df.drop(indices, axis=0)` |
| Substituir valor | `df['col'].replace(antigo, novo)` |
| Agrupar e agregar | `df.groupby('col')['col2'].mean()` |
| Series → DataFrame | `.to_frame()` |
| Renomear coluna | `df.rename(columns={'antigo': 'novo'})` |
| Criar coluna numérica | `df['nova'] = df['a'] + df['b']` |
| Criar coluna de texto | `df['nova'] = df['a'] + ' em ' + df['b']` |
| Criar coluna condicional | `df['nova'] = df['col'].apply(lambda x: 'Sim' if x > 0 else 'Não')` |
| Converter tipo | `df['col'].astype(str)` / `.astype(int)` |
| Salvar CSV | `df.to_csv('arquivo.csv', index=False, sep=';')` |
| Plotar gráfico | `df.plot(kind='bar')` |
