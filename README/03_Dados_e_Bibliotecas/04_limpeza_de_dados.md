# 🧹 Limpeza e Preparação de Dados em Python

> Dado sujo = análise errada. Antes de analisar, você precisa limpar.

---

## 1. Por que Limpar Dados?

Na vida real, dados raramente chegam perfeitos. Os problemas mais comuns:

| Problema | Exemplo |
|---|---|
| Valores ausentes | Passageiro sem idade registrada |
| Dados duplicados | Mesma venda registrada duas vezes |
| Valores inconsistentes | "masculino", "Masculino", "M" na mesma coluna |
| Formatos incorretos | Data como "15/01/2024" em vez de `datetime` |

---

## 2. Explorando o Dataset Primeiro

Antes de limpar, você precisa **entender o que tem**:

```python
import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
```

### `df.head()` — primeiras linhas

```python
df.head()      # 5 primeiras linhas (padrão)
df.head(10)    # 10 primeiras linhas
```

### `df.info()` — estrutura do dataset

```python
df.info()
```

```
RangeIndex: 891 entries
 #   Column       Non-Null Count  Dtype
 0   PassengerId  891 non-null    int64
 1   Age          714 non-null    float64   ← 891 - 714 = 177 valores ausentes
 2   Cabin        204 non-null    object    ← 687 ausentes — coluna problemática
```

Aqui você vê de cara: quantas linhas tem, o tipo de cada coluna e quantos valores **não** são nulos.

### `df.describe()` — estatísticas gerais

```python
df.describe()
```

Mostra de uma vez: contagem, média, desvio padrão, mínimo, máximo e percentis de todas as colunas numéricas.

---

## 3. Tratando Valores Ausentes (NaN)

**NaN = Not a Number** — é como o Pandas representa "dado que não existe".

### Descobrindo onde estão

```python
df.isnull().sum()
```

```
Age       177   ← 177 linhas sem idade
Cabin     687   ← 687 linhas sem cabine
Embarked    2   ← só 2 linhas sem porto
```

`isnull()` marca `True` onde é NaN. `.sum()` soma os `True` por coluna.

---

### Opção 1: Remover as linhas com NaN

```python
df_limpo = df.dropna()
```

Remove **toda linha que tiver pelo menos um NaN**.

> ⚠️ Cuidado: o Titanic tinha 891 linhas e 687 sem cabine.
> Usar `dropna()` aqui jogaria fora a maioria dos dados.
> Use só quando a quantidade de NaN for pequena.

---

### Opção 2: Preencher com a média (fillna)

```python
df["Age"] = df["Age"].fillna(df["Age"].mean())
```

**O que está acontecendo aqui:**

- `df["Age"].mean()` → calcula a média das idades que existem (ex: 29.7)
- `.fillna(29.7)` → substitui cada NaN por 29.7

Antes:
```
0    22.0
1    38.0
2    26.0
5    NaN    ← sem idade
```

Depois:
```
0    22.0
1    38.0
2    26.0
5    29.7   ← substituído pela média
```

**Por que usar a média?** Porque é uma estimativa razoável. Você não sabe a idade real, mas a média é melhor que jogar a linha fora ou colocar zero.

Outras opções de preenchimento:
```python
df["Age"].fillna(df["Age"].median())   # mediana — melhor quando tem outliers
df["Age"].fillna(0)                    # zero
df["Age"].fillna("Desconhecido")       # texto (pra colunas string)
df["Embarked"].fillna("S")             # valor mais comum
```

---

## 4. Normalização — Colocando na Mesma Escala

### Por que normalizar?

Imagine duas colunas: `Age` (0 a 80) e `Fare` (0 a 512).
Modelos de ML e comparações ficam distorcidos porque `Fare` tem valores muito maiores.
Normalizar coloca tudo entre 0 e 1, na mesma escala.

### A fórmula (Min-Max Normalization)

```python
df["Fare_normalized"] = (df["Fare"] - df["Fare"].min()) / (df["Fare"].max() - df["Fare"].min())
```

**Entendendo a fórmula:**

```
valor_normalizado = (valor - mínimo) / (máximo - mínimo)
```

Exemplo com `Fare`:
- Mínimo = 0, Máximo = 512
- Passageiro pagou 7.25 → (7.25 - 0) / (512 - 0) = **0.014** (quase zero)
- Passageiro pagou 512 → (512 - 0) / (512 - 0) = **1.0** (o máximo)

O menor valor sempre vira 0, o maior sempre vira 1. Todo mundo no meio fica proporcional.

---

## 5. Transformando Colunas com `apply`

`apply` aplica uma função em cada valor de uma coluna:

```python
df["Age_log"] = df["Age"].apply(lambda x: x)   # copia a coluna (exemplo simples)
```

Mais útil na prática:

```python
# converter texto pra minúsculo
df["Sex"] = df["Sex"].apply(lambda x: x.lower())

# categorizar por faixa etária
df["faixa"] = df["Age"].apply(lambda x: "criança" if x < 18 else "adulto")
```

`lambda x: ...` é uma função anônima — pega cada valor `x` e retorna o resultado.

---

## 6. Pipeline — Automatizando a Limpeza

Em vez de rodar cada passo manualmente, você cria uma função que faz tudo de uma vez:

```python
def limpar_dados(df):
    # 1. preenche idades ausentes com a média
    df["Age"] = df["Age"].fillna(df["Age"].mean())

    # 2. normaliza o valor da tarifa
    df["Fare_normalized"] = (
        df["Fare"] - df["Fare"].min()
    ) / (df["Fare"].max() - df["Fare"].min())

    return df


def validar_dataset(df):
    print("Linhas:", df.shape[0])
    print("Colunas:", df.shape[1])
    print("\nValores ausentes:")
    print(df.isnull().sum())


# uso
df = pd.read_csv(url)
df = limpar_dados(df)
validar_dataset(df)
```

Isso é um **pipeline de dados** — um fluxo automatizado de carregar → limpar → transformar → validar.
Em projetos reais você vai rodar isso toda vez que chegar dado novo.

---

## 7. Resumo — O Fluxo de Limpeza

```python
# 1. carrega
df = pd.read_csv("dados.csv")

# 2. explora
df.head()
df.info()
df.describe()

# 3. descobre NaN
df.isnull().sum()

# 4. trata NaN
df["coluna"] = df["coluna"].fillna(df["coluna"].mean())   # preenche
df = df.dropna(subset=["coluna_critica"])                  # ou remove só linhas críticas

# 5. remove duplicatas
df = df.drop_duplicates()

# 6. normaliza (quando necessário)
df["col_norm"] = (df["col"] - df["col"].min()) / (df["col"].max() - df["col"].min())

# 7. valida
print(df.isnull().sum())   # deve ser tudo zero nas colunas tratadas
print(df.shape)            # confere quantas linhas sobraram
```

---

## 8. Dica Importante

> **Nunca limpe os dados sem entender o contexto.**
> - `dropna()` é rápido, mas você pode perder dados valiosos
> - `fillna(mean)` é seguro pra quantidade, mas distorce um pouco a distribuição
> - Normalização é necessária pra ML, mas desnecessária pra dashboards simples
>
> Sempre verifique **quantas linhas você perde** antes de remover NaN em massa.
