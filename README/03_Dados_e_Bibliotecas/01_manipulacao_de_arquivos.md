# 📁 Trabalhando com Arquivos e Dados Externos em Python

> Ler, criar, manipular e buscar dados de qualquer fonte — tudo via Python

---

## 1. A Ideia Geral

Python consegue se conectar a praticamente qualquer fonte de dados:

| Fonte | Usado pra |
|---|---|
| `.txt` | Logs, textos simples, configurações |
| `.csv` | Tabelas, planilhas, dados estruturados |
| `.json` | APIs, configurações, dados da web |
| `.db` (SQLite) | Banco de dados local sem servidor |
| APIs externas | Dados em tempo real (clima, crypto, etc.) |

---

## 2. Arquivos de Texto (.txt)

### O `open()` e o `with`

`open()` cria a conexão entre o Python e o arquivo.
`with` garante que o arquivo seja **fechado automaticamente** ao terminar — sem risco de deixar aberto.

```python
with open("arquivo.txt", "modo") as arquivo:
    # faz o que precisar aqui
    # ao sair do bloco, fecha sozinho
```

**Os modos:**

| Modo | O que faz |
|---|---|
| `"r"` | Lê o arquivo (padrão) |
| `"w"` | Escreve — **apaga tudo** que tinha antes. Se não existir, cria. |
| `"a"` | Adiciona conteúdo no final sem apagar o que já tinha |

---

### Criando e escrevendo

```python
with open("dados.txt", "w") as arquivo:
    arquivo.write("Python é uma linguagem poderosa")
# se o arquivo não existia, foi criado
# se existia, o conteúdo anterior foi apagado
```

### Lendo tudo de uma vez

```python
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
```

### Lendo linha por linha

```python
with open("dados.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())   # strip() remove o \n do final de cada linha
```

### Adicionando sem apagar

```python
with open("dados.txt", "a") as arquivo:
    arquivo.write("\nC também é uma linguagem poderosa")
```

---

## 3. Arquivos CSV

CSV = valores separados por vírgula. É como uma planilha em texto puro.

### Criando um CSV

```python
import csv

dados = [
    ["nome", "idade", "cidade"],       # cabeçalho
    ["Ana", 25, "São Paulo"],
    ["Carlos", 30, "Rio de Janeiro"],
    ["Maria", 28, "Belo Horizonte"]
]

with open("pessoas.csv", "w", newline="") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerows(dados)   # escreve todas as linhas de uma vez
```

**O que cada parte faz:**
- `newline=""` → evita linhas em branco extras no Windows
- `csv.writer` → objeto que sabe formatar e separar os dados corretamente
- `writerows` → escreve uma lista de linhas de uma vez só

### Lendo um CSV

```python
import csv

with open("pessoas.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha)   # cada linha vira uma lista Python
```

> 💡 Na prática, CSV com Python quase sempre é feito com **Pandas** —
> muito mais poderoso. O `csv` nativo é o básico pra entender o conceito.

---

## 4. Arquivos JSON

JSON = formato de dados baseado em dicionário. É o padrão da internet.

### Criando um JSON

```python
import json

dados = {
    "nome": "Ana",
    "idade": 25,
    "cidade": "São Paulo"
}

with open("usuario.json", "w") as arquivo:
    json.dump(dados, arquivo)   # dicionário Python → arquivo JSON
```

- `json.dump(dados, arquivo)` → pega o dicionário e salva no arquivo

### Lendo um JSON

```python
import json

with open("usuario.json", "r") as arquivo:
    dados = json.load(arquivo)   # arquivo JSON → dicionário Python

print(dados)           # {'nome': 'Ana', 'idade': 25, 'cidade': 'São Paulo'}
print(dados["nome"])   # Ana
```

- `json.load(arquivo)` → transforma o JSON de volta em dicionário Python

---

## 5. APIs Externas

API = uma "porta" padronizada que um sistema abre pra outro sistema buscar dados.
Você manda uma requisição, ele te devolve dados (geralmente em JSON).

**Exemplos reais:** previsão do tempo, cotação de crypto, dados de usuários, mapas.

### Fazendo uma requisição GET

```python
import requests

url = "https://api.agify.io/?name=ana"

resposta = requests.get(url)      # GET = buscar dados

print(resposta.status_code)       # 200 = ok, 404 = não encontrado
print(resposta.text)              # resposta crua em texto
```

### Transformando em dicionário e usando os dados

```python
import requests

url = "https://api.agify.io/?name=ana"

resposta = requests.get(url)
dados = resposta.json()           # JSON da API → dicionário Python

print(dados["name"])              # ana
print(dados["age"])               # idade estimada
print(dados["count"])             # registros usados pra estimar
```

### Salvando a resposta da API em arquivo

```python
import json
import requests

url = "https://api.agify.io/?name=ana"

resposta = requests.get(url)
dados = resposta.json()

with open("dados_api.json", "w") as arquivo:
    json.dump(dados, arquivo)
# agora os dados estão salvos localmente
```

---

## 6. Banco de Dados com SQLite

SQLite = banco de dados que fica num arquivo `.db` no seu computador.
Não precisa instalar nada, já vem com Python.

### Conceitos

- `sqlite3.connect()` → abre (ou cria) a conexão com o banco
- `cursor` → o "braço" que envia comandos SQL pro banco e traz resultados
- `conexao.commit()` → confirma as alterações (sem isso, não salva)

### Criando o banco e uma tabela

```python
import sqlite3

conexao = sqlite3.connect("dados.db")   # cria o arquivo se não existir
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE usuarios (
        nome TEXT,
        idade INTEGER
    )
""")

conexao.commit()   # salva a criação da tabela
```

### Inserindo dados

```python
import sqlite3

conexao = sqlite3.connect("dados.db")
cursor = conexao.cursor()

cursor.execute(
    "INSERT INTO usuarios VALUES (?, ?)",
    ("Ana", 25)   # ? evita SQL injection — nunca coloque valor direto na string
)

conexao.commit()
```

> ⚠️ **Por que `?` em vez de f-string?**
> Nunca faça `f"INSERT INTO usuarios VALUES ('{nome}', {idade})"`.
> O `?` com tupla é a forma segura — evita SQL injection.

### Lendo os dados

```python
import sqlite3

conexao = sqlite3.connect("dados.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM usuarios")

dados = cursor.fetchall()   # traz todos os resultados como lista de tuplas

print(dados)   # [('Ana', 25), ...]
```

---

## 7. Resumo — Qual Usar Quando?

| Fonte | Quando usar |
|---|---|
| `.txt` | Logs, textos simples, scripts rápidos |
| `.csv` | Dados tabulares, planilhas, exportar pra Excel |
| `.json` | Dados de APIs, configurações, estruturas aninhadas |
| API | Dados em tempo real que mudam sempre |
| SQLite | Dados que precisam de consultas, filtros, relações |

---

## 8. O Fluxo Completo (API → Arquivo)

```python
import json
import requests

# 1. busca da API
resposta = requests.get("https://api.agify.io/?name=guilherme")
dados = resposta.json()

# 2. usa os dados
print(f"Nome: {dados['name']}, Idade estimada: {dados['age']}")

# 3. salva localmente
with open("resultado.json", "w") as arquivo:
    json.dump(dados, arquivo)

# 4. lê de volta quando precisar
with open("resultado.json", "r") as arquivo:
    dados_salvos = json.load(arquivo)
    print(dados_salvos)
```
