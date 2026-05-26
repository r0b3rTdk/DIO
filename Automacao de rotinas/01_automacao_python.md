# ⚙️ Automação de Processos e Análise com Python

> Scripts que rodam sozinhos, coletam dados, analisam e geram relatório — sem você tocar

---

## 1. O que é Automação?

Automação = você escreve o script uma vez, e ele roda sozinho no horário que você definir.

**Fluxo real:**
```
Script Python → coleta dados → processa → salva resultado → repete automaticamente
```

Exemplos práticos: relatório diário de vendas, coleta de preços de API, backup de banco de dados às 3h da manhã.

---

## 2. Lendo e Processando Arquivos Automaticamente

```python
total = 0

# escreve os dados
with open("vendas.txt", "w") as f:
    f.write("100\n200\n150\n300")

# lê e processa automaticamente
with open("vendas.txt", "r") as f:
    for linha in f:
        valor = int(linha.strip())
        total += valor

print("Total de vendas:", total)   # 750
```

O script não espera input do usuário — ele lê, calcula e entrega o resultado sozinho.

---

## 3. Coletando Dados de API Automaticamente

```python
import requests

url = "https://api.agify.io/?name=ana"

resposta = requests.get(url)
dados = resposta.json()

print(dados)   # {'count': 263051, 'name': 'ana', 'age': 54}
```

Em vez de entrar num site manualmente, o script busca os dados direto da fonte.

---

## 4. Banco de Dados SQLite — Fluxo Completo

```python
import sqlite3

# conecta (ou cria o banco)
conn = sqlite3.connect("dados.db")
cursor = conn.cursor()

# cria a tabela só se não existir
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        nome TEXT,
        idade INTEGER
    )
""")
conn.commit()

# insere dado
cursor.execute("INSERT INTO usuarios VALUES (?, ?)", ("Ana", 25))
conn.commit()

# lê os dados
cursor.execute("SELECT * FROM usuarios")
dados = cursor.fetchall()

for usuario in dados:
    print(usuario)

# SEMPRE fecha a conexão no final
conn.close()
```

> ⚠️ `CREATE TABLE IF NOT EXISTS` — sem isso, o script quebraria na segunda execução
> tentando criar uma tabela que já existe.

---

## 5. Logging vs Print — Por que Usar Logging?

Essa é uma das perguntas mais importantes da fase.

### O problema com `print()`

```python
print("Processo iniciado")      # aparece no terminal
print("Total calculado:", 750)  # some quando você fecha o terminal
```

`print()` é temporário. Quando o script roda automaticamente às 3h da manhã
e dá algum problema, você não tem como saber o que aconteceu — não havia ninguém
olhando o terminal.

### O que `logging` resolve

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="automacao.log",                          # salva em arquivo
    format="%(asctime)s - %(levelname)s - %(message)s" # com data e hora
)

logging.info("Script iniciado")
logging.warning("Dado ausente detectado")
logging.error("Falha ao conectar na API")
```

O arquivo `automacao.log` vai ter:
```
2024-01-15 08:00:01 - INFO - Script iniciado
2024-01-15 08:00:03 - WARNING - Dado ausente detectado
2024-01-15 08:00:04 - ERROR - Falha ao conectar na API
```

Você acorda de manhã, abre o arquivo de log e sabe exatamente o que aconteceu,
quando aconteceu e qual foi o nível do problema.

### Comparativo direto

| | `print()` | `logging` |
|---|---|---|
| Salva em arquivo | ❌ | ✅ |
| Mostra data e hora | ❌ | ✅ |
| Nível de severidade | ❌ | ✅ (DEBUG, INFO, WARNING, ERROR) |
| Filtra por nível | ❌ | ✅ |
| Útil em produção | ❌ | ✅ |
| Útil pra debugar rápido | ✅ | ✅ |

### Regra prática

> **Durante desenvolvimento:** `print()` é ok pra testar rápido.
> **Em código que vai rodar automaticamente:** sempre `logging`.

---

## 6. Agendando Scripts — Cron Job (Linux)

Cron job = agendador de tarefas do Linux. Define quando o script vai rodar sozinho.

```
# sintaxe:
# minuto hora dia_do_mes mês dia_da_semana comando

0 8 * * * python relatorio.py
```

Lendo:
- `0` → minuto 0
- `8` → às 8h
- `* * *` → todos os dias, todos os meses, qualquer dia da semana

Outros exemplos:
```
0 8 * * 1        # toda segunda-feira às 8h
0 */6 * * *      # a cada 6 horas
30 23 * * *      # todo dia às 23h30
0 8 1 * *        # todo dia 1 de cada mês às 8h
```

---

## 7. Registrando Data e Hora da Execução

```python
import datetime

def executar_relatorio():
    agora = datetime.datetime.now()
    print("Relatório gerado em:", agora)
    # 2024-01-15 08:00:01.234567

executar_relatorio()
```

Útil pra saber exatamente quando o script rodou — especialmente em automações agendadas.

---

## 8. Pipeline Completo com Pandas

```python
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def pipeline_restaurante():

    # 1. coleta
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
    df = pd.read_csv(url)
    logging.info("Dados coletados: %s linhas", len(df))

    # 2. analisa
    total_gorjetas = df["tip"].sum()
    gorjetas_por_dia = df.groupby("day")["tip"].sum()
    logging.info("Total de gorjetas: %s", total_gorjetas)

    # 3. salva resultado
    relatorio = pd.DataFrame({"total_gorjetas": [total_gorjetas]})
    relatorio.to_csv("relatorio_gorjetas.csv", index=False)
    logging.info("Relatório salvo em relatorio_gorjetas.csv")

    print("Pipeline executado com sucesso")
    print("Total de gorjetas:", total_gorjetas)
    print(gorjetas_por_dia)

pipeline_restaurante()
```

**O fluxo de todo pipeline:**
```
1. Coleta    → API, CSV, banco, arquivo
2. Processa  → filtra, agrupa, calcula
3. Salva     → novo CSV, banco, JSON
4. Registra  → logging com data e hora
```

---

## 9. Resumo Rápido

| Conceito | O que faz |
|---|---|
| `open()` + `with` | Lê/escreve arquivos automaticamente |
| `requests.get()` | Busca dados de API |
| `sqlite3` | Banco de dados local |
| `CREATE TABLE IF NOT EXISTS` | Evita erro na segunda execução |
| `datetime.datetime.now()` | Registra quando o script rodou |
| `logging` | Registra eventos em arquivo com data/hora |
| Cron job | Agenda o script pra rodar sozinho |
| Pipeline | Função que encapsula todo o fluxo: coleta → processa → salva |
