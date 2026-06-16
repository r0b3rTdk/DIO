# 🤖 Python + IA Avançado — JSON, LLMs Locais e Modularização

---

## 1. `join()` — Unindo Listas de Textos em Uma String

`join()` une todos os itens de uma lista em uma única string, com um separador escolhido por você.

```python
resenhas = ["Produto quebrado.", "Chegou errado.", "Não funcionou."]

# Une com separador
texto = "#####".join(resenhas)
# "Produto quebrado.#####Chegou errado.#####Não funcionou."

# Outros separadores comuns
", ".join(["a", "b", "c"])     # "a, b, c"
"\n".join(["linha1", "linha2"]) # "linha1\nlinha2"
" | ".join(["x", "y", "z"])    # "x | y | z"
```

**Por que usar separador incomum como `#####`?** Para garantir que o separador não apareça dentro do conteúdo das resenhas — vírgulas e espaços podem aparecer no texto, `#####` dificilmente aparece.

---

## 2. `split()` — Quebrando String em Lista

`split()` é o inverso do `join()` — divide uma string em lista usando um separador.

```python
# Separando categorias retornadas pela IA
categorias_texto = "durabilidade, desempenho, compatibilidade, design, embalagem"
lista_categorias = categorias_texto.split(", ")
# ['durabilidade', 'desempenho', 'compatibilidade', 'design', 'embalagem']

# Separando por outro delimitador
"a#####b#####c".split("#####")
# ['a', 'b', 'c']
```

---

## 3. Pipeline — Filtrar DataFrame → Juntar → Enviar para IA

```python
# 1. Filtra só as negativas
df_negativas = df_reviews[df_reviews["Análises de Sentimentos"] == "Negativa"]

# 2. Extrai a coluna de texto
resenhas_negativas = df_negativas["reviewText"]

# 3. Une tudo em uma string
resenhas_unidas = "#####".join(resenhas_negativas)

# 4. Envia para a IA
resposta = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""Você é analista de dados. Vou te passar resenhas negativas separadas por '#####'.
Encontre 5 categorias de reclamações. Retorne APENAS as 5 categorias,
separadas por vírgula, em minúsculo, sem acentos.

Exemplo: 'eletronicos, roupas, alimentos, viagens, brinquedos'

Resenhas: {resenhas_unidas}"""
)

# 5. Converte resultado em lista Python
categorias = resposta.text.split(", ")
```

---

## 4. JSON — Formato de Dados da Internet

JSON (JavaScript Object Notation) é o formato padrão de troca de dados na web. É praticamente idêntico a um dicionário Python:

```json
{
    "resenha_original": "I didn't like the color",
    "resenha_pt": "Eu não gostei da cor",
    "categoria": "design"
}
```

Pode conter listas também:
```json
[
    {"nome": "Ana", "nota": 8.5},
    {"nome": "João", "nota": 7.0}
]
```

### Convertendo JSON (string) → Python (dict/list)

```python
import json

# String JSON → dicionário/lista Python
dados = json.loads('{"nome": "Ana", "nota": 8.5}')
print(dados["nome"])   # Ana

# Dicionário Python → string JSON
texto = json.dumps({"nome": "Ana", "nota": 8.5})
```

### Limpando a resposta da IA antes de converter

A IA às vezes retorna o JSON dentro de blocos de código markdown:
````
```json
{"chave": "valor"}
```
````

```python
# Remove os marcadores markdown antes de converter
json_limpo = resposta.replace("```json", "").replace("```", "").strip()
dados = json.loads(json_limpo)
```

### Pedindo JSON estruturado à IA

```python
resposta = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""Analise estas resenhas negativas (separadas por '#####') e retorne um JSON no formato:
[
    {{
        "resenha_original": "texto original",
        "resenha_pt": "tradução em português",
        "categoria": "categoria"
    }}
]

Retorne APENAS o texto JSON. Nada mais.

Resenhas: {resenhas_unidas}"""
)

json_limpo = resposta.text.replace("```json", "").replace("```", "").strip()
lista_classificada = json.loads(json_limpo)
print(len(lista_classificada))   # quantidade de resenhas classificadas
```

---

## 5. Rodando LLMs Localmente — LM Studio

Quando usar local em vez de API externa:
- Dados sensíveis que não podem sair da máquina
- Sem limite de tokens ou custo por chamada
- Fine-tuning de modelos especializados
- Sem dependência de internet

### LM Studio

Interface visual para baixar e rodar modelos open source (LLaMA, Gemma, DeepSeek...).

1. Baixe em `lmstudio.ai`
2. Na aba "Discover", baixe um modelo (sugestão: **Gemma 3 1B** — roda na maioria das máquinas)
3. Carregue o modelo → ele fica disponível em `http://127.0.0.1:1234`

### Conectando Python ao LM Studio

O LM Studio usa o mesmo padrão da API da OpenAI — você aponta a `base_url` pro servidor local:

```python
from openai import OpenAI

client_local = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"        # qualquer string — só pra não dar erro de autenticação
)

resposta = client_local.chat.completions.create(
    model="google/gemma-3-1b",
    messages=[
        {"role": "system", "content": "Você é um assistente útil."},
        {"role": "user",   "content": "O que é IA Generativa?"}
    ],
    temperature=0.7,
    max_tokens=500,
)

print(resposta.choices[0].message.content)
```

---

## 6. O Padrão OpenAI SDK

A OpenAI estabeleceu um padrão de API que muitos outros serviços adotam. Isso significa que você pode usar a mesma biblioteca `openai` com:

| Serviço | `base_url` | `api_key` |
|---|---|---|
| OpenAI (oficial) | (padrão) | sua chave |
| Groq | `https://api.groq.com/openai/v1` | chave do Groq |
| LM Studio (local) | `http://127.0.0.1:1234/v1` | `"lm-studio"` |
| Ollama (local) | `http://localhost:11434/v1` | `"ollama"` |

```python
# Mesmo código, só muda base_url e api_key
from openai import OpenAI

client = OpenAI(base_url="URL_DO_SERVIÇO", api_key="CHAVE")
```

---

## 7. Ambiente Virtual — `venv`

Ao trabalhar localmente (fora do Colab), use ambiente virtual para isolar dependências do projeto.

```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar (Windows)
.venv\Scripts\Activate

# Ativar (Mac/Linux)
source .venv/bin/activate

# Instalar bibliotecas
pip install openai pandas

# Desativar
deactivate
```

**Por que usar?** Cada projeto pode precisar de versões diferentes das bibliotecas. O `venv` isola isso — o que você instala num projeto não afeta outros.

---

## 8. Modularização — Dividindo o Código em Arquivos

Em vez de tudo num arquivo só, separe por responsabilidade:

```
projeto/
├── main.py          ← execução principal
├── ai_utils.py      ← funções que chamam a IA
├── data_utils.py    ← funções que manipulam dados
└── file_utils.py    ← funções de leitura/escrita
```

```python
# ai_utils.py
from google import genai

def analisar_sentimento(texto: str) -> str:
    client = genai.Client()
    resposta = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Classifique: {texto}. Responda só: Positiva, Negativa ou Neutra."
    )
    return resposta.text.strip()
```

```python
# main.py
from ai_utils import analisar_sentimento

resultado = analisar_sentimento("Adorei o produto!")
print(resultado)   # Positiva
```

**Vantagens:**
- Fácil de testar cada parte separado
- Fácil de reutilizar em outros projetos
- Equipes diferentes podem trabalhar em arquivos diferentes sem conflito

---

## 9. Resumo Rápido

| O que fazer | Como fazer |
|---|---|
| Unir lista em string | `"sep".join(lista)` |
| Quebrar string em lista | `texto.split("sep")` |
| String JSON → dict Python | `json.loads(texto)` |
| Dict Python → string JSON | `json.dumps(dados)` |
| Limpar markdown da IA | `.replace("```json", "").replace("```", "")` |
| Rodar LLM local | LM Studio + `OpenAI(base_url="http://127.0.0.1:1234/v1")` |
| Isolar dependências | `python -m venv .venv` |
| Separar código em módulos | Arquivos `.py` separados + `from arquivo import funcao` |
