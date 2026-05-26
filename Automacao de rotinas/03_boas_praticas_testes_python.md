# 🧼 Boas Práticas, Testes e Performance em Python

---

## 1. O que você já sabe (revisão rápida)

- **Clean code** → nomes claros, funções pequenas, sem "mágica"
- **Modularização** → separar responsabilidades em arquivos (`utils.py`, `main.py`)
- **Refatoração** → melhorar o código sem mudar o que ele faz

```python
# antes
def processar(lista):
    resultado = []
    for i in lista:
        if i > 10:
            resultado.append(i * 2)
    return resultado

# depois — list comprehension
def processar_numeros(lista):
    return [numero * 2 for numero in lista if numero > 10]
```

---

## 2. Assert — Teste Simples e Direto

`assert` verifica se uma condição é verdadeira.
Se for verdadeira, não faz nada. Se for falsa, joga `AssertionError`.

```python
def soma(a, b):
    return a + b

assert soma(2, 3) == 5    # passa — sem ruído
assert soma(2, 2) == 5    # AssertionError — falhou!
```

**Pra que serve?** Testar rapidamente se uma função está funcionando como esperado,
sem precisar de `print()` ou verificação manual.

### Com pytest — testes automatizados

Pytest é a ferramenta padrão de testes em Python.
Você cria funções que começam com `test_` e ele roda tudo automaticamente.

```python
# arquivo: test_utils.py

def soma(a, b):
    return a + b

def test_soma_positivos():
    assert soma(2, 3) == 5

def test_soma_negativos():
    assert soma(-1, -1) == -2

def test_soma_zero():
    assert soma(0, 5) == 5
```

No terminal:
```bash
pytest test_utils.py
```

Saída:
```
...,    ← 3 pontos = 3 testes passaram
3 passed in 0.01s
```

Se um teste falhar:
```
FAILED test_utils.py::test_soma_positivos - AssertionError
```

> 💡 **Por que testar?** Porque quando você mudar o código depois,
> os testes avisam automaticamente se algo quebrou. Sem testes,
> você só descobre o erro em produção — tarde demais.

---

## 3. Medindo Performance com `time`

```python
import time

inicio = time.time()   # marca o início

for i in range(1_000_000):
    pass

fim = time.time()      # marca o fim

print("Tempo:", fim - inicio, "segundos")   # ex: 0.05s
```

Útil pra comparar duas implementações e ver qual é mais rápida.

### Exemplo: loop vs função nativa

```python
import time

numeros = list(range(1_000_000))

# com loop manual
inicio = time.time()
total = 0
for n in numeros:
    total += n
print("Loop:", time.time() - inicio)   # ~0.08s

# com sum() nativo
inicio = time.time()
total = sum(numeros)
print("sum():", time.time() - inicio)  # ~0.02s — 4x mais rápido
```

**Por que funções nativas são mais rápidas?** Porque são implementadas em C por baixo.
Sempre prefira `sum()`, `max()`, `min()`, `len()` a loops manuais equivalentes.

---

## 4. Estrutura de Projeto Organizada

```
projeto/
│
├── src/
│   ├── main.py       ← execução principal
│   └── utils.py      ← funções reutilizáveis
│
├── tests/
│   └── test_utils.py ← testes automatizados
│
├── data/             ← arquivos de dados
└── requirements.txt  ← bibliotecas necessárias
```

`requirements.txt` lista as bibliotecas do projeto:
```
pandas==2.0.0
numpy==1.24.0
matplotlib==3.7.0
```

Pra instalar tudo: `pip install -r requirements.txt`

---

## ⚠️ Sobre a Parte de Métricas que Você Pulou

Você disse que pulou porque "não pareceu tão importante".
**Foi o erro maior do módulo.**

O código que você viu no final do notebook faz isso:

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

Isso é **a base de Machine Learning**. Sem entender:
- por que dividir dados em treino e teste
- o que é overfitting e underfitting
- como medir se um modelo é bom

...você não consegue avançar em ML. Esses conceitos aparecem em **todo modelo** que você vai construir daqui pra frente.

**Volte nesse conteúdo e mande pra mim. Vou resumir direito.**
