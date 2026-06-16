# 🐼 Pandas Avançado — loc, iloc, set_index e tqdm

---

## 1. `loc` e `iloc` — Selecionando Linhas e Colunas

São os dois métodos de seleção precisa do Pandas. A diferença é simples:

| | `iloc` | `loc` |
|---|---|---|
| Acessa por | **Posição numérica** (0, 1, 2...) | **Rótulo/nome** (texto, data...) |
| Índice padrão | ✅ Sempre funciona | ✅ Funciona quando índice é texto |
| Analogia | Linha do Excel pelo número | Célula do Excel pelo nome (B5, D12) |

---

### `iloc` — por posição numérica

```python
df.iloc[15]          # linha de índice 15
df.iloc[0:16]        # linhas 0 até 15 (16 não incluso)
df.iloc[34:42]       # linhas 34 até 41
df.iloc[43:]         # da linha 43 até o final
df.iloc[-1]          # última linha
```

---

### `loc` — por rótulo (texto, data, etc.)

Funciona melhor quando o índice é texto. Para isso, primeiro converte uma coluna para índice com `set_index()`:

```python
# Converte coluna 'Nome do produto' para ser o índice
df_indexado = df.set_index("Nome do produto")

# Agora acessa por nome
df_indexado.loc["Produto 15"]
df_indexado.loc["Produto 15":"Produto 35"]   # intervalo
df_indexado.loc["Produto 45":]               # do 45 até o final
```

---

### Selecionando linha + coluna específica

```python
# Uma célula específica (linha + coluna)
df_indexado.loc["Produto 45", "Preço do produto"]
# Equivale a: B45 no Excel

# Lista de linhas + lista de colunas
df_indexado.loc[
    ["Produto 45", "Produto 47", "Produto 16"],
    ["Preço do produto", "Itens vendidos"]
]
```

---

### `loc` + filtro booleano — combinação poderosa

```python
# Filtra os eletrônicos
eletronicos = df_indexado[df_indexado["Categoria do produto"] == "Eletrônicos"]

# Pega só colunas específicas dos eletrônicos
df_indexado.loc[eletronicos.index, ["Preço do produto", "Itens vendidos"]]
```

---

### Alterando valores com `loc`

```python
# Renomeia toda a categoria "Brinquedos" para "Infanto-juvenil"
brinquedos = df_indexado[df_indexado["Categoria do produto"] == "Brinquedos"]
df_indexado.loc[brinquedos.index, "Categoria do produto"] = "Infanto-juvenil"

# Confirma que não existe mais "Brinquedos"
df_indexado["Categoria do produto"].unique()
```

---

## 2. `set_index()` — Transformando Coluna em Índice

Por padrão, o Pandas cria índices numéricos (0, 1, 2...). Com `set_index()` você usa uma coluna como índice:

```python
# Antes: índice numérico
df.head()
#    Nome do produto  Preço
# 0  Produto 1        150.0
# 1  Produto 2        320.0

# Depois: índice textual
df_indexado = df.set_index("Nome do produto")
df_indexado.head()
#              Preço
# Produto 1    150.0
# Produto 2    320.0
```

### Voltando ao índice numérico — `reset_index()`

```python
df_original = df_indexado.reset_index()
# A coluna "Nome do produto" volta a ser coluna normal
```

**Quando usar `set_index`?** Quando o conteúdo da coluna é único e vai ser usado como chave de busca frequente (nome, CPF, código do produto, data).

---

## 3. NumPy — Geração de Dados Aleatórios

Muito usado pra criar DataFrames de teste:

```python
import numpy as np

# Escolha aleatória de categorias (com repetição)
categorias = np.random.choice(["Eletrônicos", "Livros", "Roupas"], 50)

# Números decimais aleatórios entre 10 e 500
precos = np.random.uniform(10.0, 500.0, 50).round(2)

# Inteiros aleatórios entre 1 e 1000
vendas = np.random.randint(1, 1000, 50)
```

---

## 4. `tqdm` — Barra de Progresso

Quando você tem um loop que demora (chamadas à API, processamento de arquivos grandes), `tqdm` mostra uma barra de progresso visual.

```python
from tqdm import tqdm

# Sem tqdm — você não sabe o andamento
for item in lista:
    processar(item)

# Com tqdm — mostra barra de progresso
for item in tqdm(lista):
    processar(item)
```

Saída no terminal:
```
 45%|████████████           | 45/100 [00:12<00:15,  3.2it/s]
```

### Com `enumerate` + `tqdm`

```python
from tqdm import tqdm

for i, item in enumerate(tqdm(lista, desc="Processando")):
    resultado = chamar_api(item)
```

### Instalando (se precisar)

```python
!pip install tqdm
```

> 💡 No Google Colab já vem instalado. Para notebooks Jupyter, use `tqdm.notebook`:
> `from tqdm.notebook import tqdm`

---

## 5. Análise de Sentimentos com IA + Pandas

Padrão completo: percorrer uma coluna de textos, enviar cada um pra IA, salvar o resultado, adicionar como nova coluna.

```python
from google import genai
from tqdm import tqdm
import pandas as pd

client = genai.Client()

# Carrega o CSV
df_reviews = pd.read_csv("/content/reviews.csv")

# Isola a coluna de texto
coluna_reviews = df_reviews["reviewText"]

# Lista que vai acumular os resultados
lista_sentimentos = []

# Loop com barra de progresso
for resenha in tqdm(coluna_reviews, desc="Analisando sentimentos"):
    resposta = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""Você irá analisar a resenha abaixo e retornar uma análise de sentimento.
Responda APENAS com uma das palavras: 'Positiva', 'Negativa' ou 'Neutra'.

Exemplos:
"Eu adorei esse produto" -> Positiva
"Gostei, mas não é nada especial" -> Neutra
"Odiei esse produto" -> Negativa

Resenha: {resenha}"""
    )
    lista_sentimentos.append(resposta.text.strip())

# Adiciona resultado como nova coluna
df_reviews["Sentimento"] = lista_sentimentos

# Visualiza
df_reviews.head()
```

> ⚠️ O tamanho da `lista_sentimentos` precisa ser igual ao número de linhas do DataFrame.
> Se o loop quebrar no meio, as listas ficam com tamanhos diferentes e dá erro.

---

## 6. Valores Únicos de uma Coluna — Dois Jeitos

```python
# Retorna um array NumPy com os valores únicos
df["Categoria"].unique()
# array(['Eletrônicos', 'Livros', 'Roupas', 'Alimentos', 'Infanto-juvenil'])

# Retorna um set Python (sem ordem garantida)
set(df["Categoria"])
# {'Eletrônicos', 'Livros', 'Roupas', 'Alimentos', 'Infanto-juvenil'}
```

---

## 7. Resumo Rápido

| O que fazer | Como fazer |
|---|---|
| Acessar linha por posição | `df.iloc[15]` |
| Acessar intervalo por posição | `df.iloc[10:20]` |
| Acessar linha por nome | `df.loc["Produto 15"]` |
| Acessar célula específica | `df.loc["Produto 15", "Preço"]` |
| Acessar múltiplas linhas/colunas | `df.loc[lista_linhas, lista_colunas]` |
| Transformar coluna em índice | `df.set_index("coluna")` |
| Voltar ao índice numérico | `df.reset_index()` |
| Alterar valores por condição | `df.loc[filtro.index, "col"] = novo_valor` |
| Valores únicos | `df["col"].unique()` |
| Progresso em loop | `for item in tqdm(lista):` |
| Criar coluna com resultado de IA | `df["nova_col"] = lista_resultados` |
