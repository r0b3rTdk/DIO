# 📐 Métricas e Avaliação de Modelos em Machine Learning

> Treinar um modelo é fácil. Saber se ele presta é a parte difícil.

---

## 1. O Problema Central

Você treinou um modelo. Ele acerta muito nos dados que você usou pra treinar.
Mas quando chega um dado novo, erra feio.

**Isso é o problema mais comum em ML** — e é exatamente o que as métricas detectam.

---

## 2. Treino vs Teste — Por que Dividir os Dados?

Imagine que você vai fazer uma prova. Se você decorar as respostas da prova anterior,
vai bem nela — mas se a prova mudar, vai mal.

Em ML é a mesma coisa:

- **Dados de treino** → o modelo aprende com esses
- **Dados de teste** → você avalia se o modelo aprendeu de verdade

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,    # 20% pra teste, 80% pra treino
    random_state=42   # garante que a divisão seja sempre igual
)
```

**Por que 80/20?** É a proporção mais comum. Você precisa de dados suficientes
pra treinar, mas também de dados suficientes pra testar com confiança.

```
Dataset completo (100%)
       │
       ├── Treino (80%) → modelo aprende aqui
       └── Teste  (20%) → modelo é avaliado aqui (nunca viu esses dados)
```

---

## 3. Overfitting vs Underfitting

### Overfitting — decorou demais

O modelo aprendeu os dados de treino tão bem que memorizou até os ruídos.
Funciona perfeitamente no treino, mas falha em dados novos.

```
Treino:  99% de acerto  ✅
Teste:   62% de acerto  ❌  ← grande diferença = overfitting
```

**Analogia:** aluno que decorou as questões da prova anterior.
Vai bem se cair a mesma prova, péssimo se mudar qualquer coisa.

### Underfitting — aprendeu de menos

O modelo é simples demais e não consegue capturar os padrões dos dados.
Vai mal tanto no treino quanto no teste.

```
Treino:  65% de acerto  ❌
Teste:   63% de acerto  ❌  ← ambos ruins = underfitting
```

**Analogia:** aluno que não estudou. Vai mal em qualquer prova.

### O ponto ideal

```
Treino:  88% de acerto  ✅
Teste:   85% de acerto  ✅  ← próximos = generalizou bem
```

---

## 4. Regressão Linear — Prevendo Preço de Casas

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

url = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"
df = pd.read_csv(url)

# remove linhas com NaN
df = df.dropna()

# X = variáveis de entrada (tudo menos o preço)
X = df.drop("median_house_value", axis=1)

# converte colunas de texto em números (ex: "NEAR BAY" → 0 ou 1)
X = pd.get_dummies(X)

# y = o que queremos prever
y = df["median_house_value"]

# divide em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# treina o modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# avalia no teste
print("Score no treino:", modelo.score(X_train, y_train))
print("Score no teste:", modelo.score(X_test, y_test))
```

**O que está acontecendo:**
- `X` = as características da casa (quartos, localização, renda da região...)
- `y` = o preço da casa
- O modelo aprende a relação entre X e y no treino
- `score()` retorna o R² — o quão bem o modelo explica os dados (0 a 1)

---

## 5. Métricas de Regressão

Para problemas de regressão (prever um número), as métricas mais usadas são:

### MAE — Erro Médio Absoluto

```python
from sklearn.metrics import mean_absolute_error

y_pred = modelo.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print("MAE:", mae)
```

**O que significa:** em média, o modelo erra X unidades.
- MAE de 30.000 → em média, o modelo erra R$30.000 no preço da casa
- Quanto menor, melhor

### RMSE — Raiz do Erro Quadrático Médio

```python
from sklearn.metrics import mean_squared_error
import numpy as np

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("RMSE:", rmse)
```

**Diferença do MAE:** penaliza mais os erros grandes.
Use quando erros grandes são especialmente ruins no seu problema.

### R² — Coeficiente de Determinação

```python
from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_pred)
print("R²:", r2)
```

**O que significa:**
- R² = 1.0 → modelo perfeito
- R² = 0.85 → modelo explica 85% da variação dos dados
- R² < 0 → modelo pior que simplesmente usar a média

---

## 6. Métricas de Classificação

Para problemas de classificação (prever uma categoria), outras métricas:

| Métrica | O que mede |
|---|---|
| **Accuracy** | % de acertos no total |
| **Precision** | dos que previu como positivo, quantos eram de fato positivos |
| **Recall** | dos que eram positivos, quantos o modelo acertou |
| **F1-Score** | equilíbrio entre precision e recall |

```python
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
```

---

## 7. Validação Cruzada — Teste Mais Confiável

Problema do train_test_split: a divisão pode ter "sorte" ou "azar".
Validação cruzada divide os dados em K partes e testa K vezes.

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(modelo, X, y, cv=5)   # 5 divisões diferentes

print("Scores:", scores)
print("Média:", scores.mean())
print("Desvio padrão:", scores.std())
```

```
Scores: [0.63, 0.65, 0.61, 0.64, 0.62]
Média: 0.63
Desvio padrão: 0.01   ← baixo = modelo consistente
```

Se o desvio padrão for alto, o modelo é instável — vai bem em alguns dados e mal em outros.

---

## 8. Resumo — O que Checar Sempre

```
1. Treinar o modelo com os dados de treino
2. Avaliar nos dados de teste (que o modelo nunca viu)
3. Comparar treino vs teste:
   - Treino muito melhor que teste = overfitting
   - Ambos ruins = underfitting
   - Próximos e bons = generalizou bem ✅
4. Usar a métrica certa:
   - Regressão  → MAE, RMSE, R²
   - Classificação → Accuracy, F1-Score
5. Usar cross_val_score pra confirmar
```

---

## 9. Por que Isso É a Base de ML

Todo modelo de ML que você vai construir daqui pra frente segue esse fluxo:

```python
# 1. prepara os dados
X, y = preparar_dados(df)

# 2. divide
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 3. treina
modelo.fit(X_train, y_train)

# 4. avalia
score = modelo.score(X_test, y_test)
print("Score:", score)
```

Não importa se é Regressão Linear, Random Forest, Rede Neural ou qualquer outro algoritmo —
o fluxo de avaliação é sempre esse. Entender bem aqui poupa muita dor de cabeça depois.
