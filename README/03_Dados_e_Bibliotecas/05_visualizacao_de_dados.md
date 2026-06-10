# 📈 Visualização de Dados com Python

> Matplotlib, Seaborn e Plotly — do gráfico simples ao interativo animado

---

## 1. As 3 Bibliotecas e Quando Usar Cada Uma

| Biblioteca | Quando usar |
|---|---|
| `Matplotlib` | Controle total — você define cada detalhe do gráfico |
| `Seaborn` | Gráficos estatísticos bonitos com menos código |
| `Plotly` | Gráficos interativos — zoom, hover, filtros, animação |

**Regra prática:**
- Análise rápida pra você mesmo → Seaborn
- Apresentação estática → Matplotlib ou Seaborn
- Dashboard ou apresentação dinâmica → Plotly

---

## 2. Gráfico de Dispersão (Scatter)

Mostra a relação entre duas variáveis numéricas.

```python
# Matplotlib — controle manual
plt.scatter(df["total_bill"], df["tip"])
plt.xlabel("Conta total")
plt.ylabel("Gorjeta")
plt.title("Relação entre conta e gorjeta")
plt.show()
```

```python
# Seaborn — mesma coisa, menos código
sns.scatterplot(data=df, x="total_bill", y="tip")
plt.show()
```

```python
# Plotly — interativo com cor por categoria
fig = px.scatter(df, x="total_bill", y="tip", color="day", title="Conta vs Gorjeta")
fig.show()
```

**O que o scatter mostra aqui:** conforme a conta aumenta, a gorjeta tende a aumentar junto. Isso é uma **correlação positiva**.

---

## 3. Histograma — Distribuição de uma variável

**O que é distribuição?** É como os valores se espalham. Quantas contas foram entre R$10-20? Quantas entre R$20-30?

```python
sns.histplot(df["total_bill"])
plt.title("Distribuição das contas")
plt.show()
```

Imagine o eixo X como faixas de valor (10, 15, 20, 25...) e o eixo Y como a contagem — quantas vezes aquele valor apareceu. O histograma mostra se os dados são concentrados, espalhados, ou se têm um pico.

**Lendo o gráfico:**
- Barra alta = muitos clientes com aquele valor de conta
- Barra baixa = poucos clientes
- Pico no meio = a maioria das contas fica naquela faixa

---

## 4. Boxplot — Distribuição por Grupo

O boxplot é o gráfico que mais confunde no começo, mas é muito útil.

```python
sns.boxplot(data=df, x="day", y="tip")
plt.title("Gorjetas por dia")
plt.show()
```

**Lendo uma "caixa" do boxplot:**

```
         |          ← valor máximo (sem outliers)
    _____|_____
    |         |
    |  caixa  |     ← 75% dos dados ficam aqui
    |---------|     ← linha do meio = mediana (valor do meio)
    |         |     ← 25% dos dados ficam aqui
    |_________|
         |          ← valor mínimo (sem outliers)
         o          ← ponto solto = outlier (valor fora do padrão)
```

**No contexto do restaurante:**
- A caixa mostra onde ficam a maioria das gorjetas naquele dia
- A linha do meio mostra a gorjeta típica (mediana)
- Pontos soltos acima = alguém deu gorjeta muito acima do normal
- Caixa mais alta = gorjetas maiores naquele dia

**Lendo o gráfico do restaurante:**
- Domingo (Sun) e Sábado (Sat) têm gorjetas maiores — faz sentido, fim de semana
- Sexta (Fri) tem menos variação
- Os pontos soltos (outliers) são clientes muito generosos

---

## 5. Heatmap de Correlação — O que é Correlação?

```python
correlacao = df.corr(numeric_only=True)

sns.heatmap(correlacao, annot=True, cmap="coolwarm")
plt.title("Correlação entre variáveis")
plt.show()
```

**Correlação** = o quanto uma variável influencia a outra.

O valor vai de -1 a +1:

| Valor | Significa |
|---|---|
| `1.0` | Quando X sobe, Y sobe junto (perfeito) |
| `0.7` | Quando X sobe, Y tende a subir (forte) |
| `0.0` | X e Y não têm relação |
| `-0.7` | Quando X sobe, Y tende a descer (inversa) |
| `-1.0` | Quando X sobe, Y desce (inversa perfeita) |

**No heatmap do restaurante:**
- `total_bill` e `tip` → correlação ~0.68 = conta maior, gorjeta maior (faz sentido)
- `total_bill` e `size` → correlação ~0.60 = mesa maior, conta maior (faz sentido)
- As cores: vermelho = correlação positiva, azul = negativa

**Por que isso importa?** Em Machine Learning, você usa correlação pra decidir quais variáveis usar no modelo. Se duas variáveis têm correlação 0.99, você provavelmente não precisa das duas.

---

## 6. Múltiplos Gráficos com Subplots

```python
fig, ax = plt.subplots(2, 2, figsize=(12, 8))   # grade 2 linhas x 2 colunas

sns.histplot(df["total_bill"], ax=ax[0, 0])       # posição [linha, coluna]
ax[0, 0].set_title("Distribuição das contas")

sns.boxplot(data=df, x="day", y="tip", ax=ax[0, 1])
ax[0, 1].set_title("Gorjetas por dia")

sns.scatterplot(data=df, x="total_bill", y="tip", ax=ax[1, 0])
ax[1, 0].set_title("Conta vs Gorjeta")

sns.countplot(data=df, x="day", ax=ax[1, 1])
ax[1, 1].set_title("Clientes por dia")

plt.tight_layout()   # ajusta espaçamento pra não sobrepor
plt.show()
```

`ax[0,0]` → linha 0, coluna 0 (canto superior esquerdo)
`ax[1,1]` → linha 1, coluna 1 (canto inferior direito)

---

## 7. Plotly Interativo — Parâmetros Explicados

```python
fig = px.scatter(
    df,
    x="total_bill",       # eixo X
    y="tip",              # eixo Y
    color="day",          # cor diferente por dia
    size="size",          # tamanho do ponto = tamanho da mesa
    hover_data=["sex", "time"],   # mostra ao passar o mouse
    title="Conta vs Gorjeta"
)
fig.show()
```

**O que cada parâmetro faz:**
- `color="day"` → cada dia vira uma cor. Você vê de uma vez qual dia tem mais gorjeta
- `size="size"` → ponto maior = mesa com mais pessoas
- `hover_data` → ao passar o mouse no ponto, aparece sexo e horário do cliente

---

## 8. Gráfico Animado — `animation_frame`

```python
fig = px.scatter(
    df,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    animation_frame="year",   # ← isso cria a animação
    title="PIB vs Expectativa de Vida ao longo dos anos"
)
fig.show()
```

`animation_frame="year"` → cria um "play" que passa por cada ano automaticamente.
Você vê como os países evoluíram ao longo do tempo — cada frame é um ano diferente.

---

## 9. `facet_col` — Dividindo em Painéis

```python
fig = px.scatter(
    df,
    x="total_bill",
    y="tip",
    color="day",
    size="size",
    facet_col="time",      # ← divide em painéis por coluna
    title="Gorjetas: Almoço vs Jantar"
)
fig.show()
```

`facet_col="time"` divide o gráfico em dois painéis lado a lado — um pra `Lunch` e outro pra `Dinner`. Assim você compara os dois contextos sem misturar os dados.

---

## 10. Mapa de Calor Geográfico (Choropleth)

```python
fig = px.choropleth(
    df,
    locations="iso_alpha",        # código do país (BRA, USA, etc.)
    color="lifeExp",              # a cor representa a expectativa de vida
    hover_name="country",         # nome do país ao passar o mouse
    animation_frame="year",       # animado por ano
    color_continuous_scale="Viridis",  # paleta de cores
    title="Expectativa de vida no mundo"
)
fig.show()
```

É um mapa-múndi onde cada país recebe uma cor baseada num valor.
Cores mais claras = expectativa de vida maior. Com `animation_frame` você vê a evolução por ano.

---

## 11. Resumo — Qual Gráfico Usar Quando?

| Pergunta que você quer responder | Gráfico ideal |
|---|---|
| Como X e Y se relacionam? | `scatter` |
| Como os valores estão distribuídos? | `histplot` |
| Como os grupos se comparam? | `boxplot` |
| Qual a frequência de cada categoria? | `countplot` / `bar` |
| Qual a correlação entre variáveis? | `heatmap` |
| Como evoluiu ao longo do tempo? | `scatter` com `animation_frame` |
| Como comparar dois grupos lado a lado? | `facet_col` |
| Mostrar dados em mapa? | `choropleth` |
