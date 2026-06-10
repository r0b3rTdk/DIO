# 🤖 Python Aplicado à IA — Gemini, Chatbots e LLMs

> Conectar Python a modelos de linguagem, criar chatbots e integrar APIs de IA

---

## 1. Configurando o Ambiente (Google Colab)

```python
import os
from google.colab import userdata

# Salva a chave de API do Gemini como variável de ambiente
os.environ['GOOGLE_API_KEY'] = userdata.get('GEMINI_API_KEY')
```

As chaves de API ficam no **Secrets** do Colab — nunca cole direto no código.

---

## 2. Pergunta Pontual com Gemini

Para uma única pergunta sem histórico:

```python
from google import genai

client = genai.Client()

resposta = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="O que é inteligência artificial?"
)

print(resposta.text)
```

---

## 3. Chat com Histórico (Memória)

Para conversas que mantêm contexto entre mensagens:

```python
# Cria o chat — mantém histórico automaticamente
chat = client.chats.create(model="gemini-2.5-flash")

# Envia mensagens
resposta = chat.send_message("O que é inteligência artificial?")
print(resposta.text)

resposta = chat.send_message("Quando foi lançado o ChatGPT?")
print(resposta.text)

# Vê o histórico completo da conversa
chat.get_history()
```

**Diferença:**
- `client.models.generate_content()` → uma pergunta, uma resposta, sem memória
- `client.chats.create()` + `chat.send_message()` → conversa com histórico

---

## 4. Chatbot Interativo com `while`

```python
prompt = input("Digite a sua pergunta: ")

while prompt != "fim":
    resposta = chat.send_message(prompt)
    print("\n")
    print(resposta.text)
    print("-" * 50)
    prompt = input("Digite a sua pergunta: ")
```

**Por que o `while` em vez do `for`?** Porque não sabemos quantas perguntas o usuário vai fazer. O `for` itera sobre uma sequência conhecida. O `while` continua enquanto uma condição for verdadeira — ideal para entrada do usuário.

> ⚠️ **Cuidado com loop infinito:** você precisa mudar o valor da variável `prompt` dentro do loop. Sem o segundo `input()` dentro do `while`, o mesmo prompt seria enviado infinitamente.

---

## 5. Resumidor de E-mails com `enumerate`

```python
def resumidor_de_emails(lista_de_emails):
    for numero, email in enumerate(lista_de_emails):
        resposta = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""Vou te mandar o corpo de um e-mail.
Quero que você o resuma em apenas 1 linha, passando o intuito daquele e-mail.
Segue o e-mail: {email}"""
        )
        print(f"E-mail {numero + 1}: {resposta.text}")
        print("-" * 50)

resumidor_de_emails(email_bodies)
```

`enumerate()` devolve o índice + o valor ao mesmo tempo — sem precisar de contador manual.
`numero + 1` porque `enumerate` começa em 0, mas queremos mostrar a partir de 1.

---

## 6. LLMs Open Source com Groq

**Groq** (com Q) = serviço que hospeda modelos open source (LLaMA, DeepSeek, GPT-OSS) com inferência extremamente rápida.

Diferente do Gemini (modelo fechado do Google), modelos open source podem ser baixados e rodados localmente — mais privacidade e sem limite de uso imposto pela empresa.

```bash
# Instalar a biblioteca
!pip install -q groq
```

```python
import os
from google.colab import userdata
from groq import Groq

os.environ["GROQ_API_KEY"] = userdata.get('GROQ_API_KEY')

client = Groq()

completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",      # modelo open source
    messages=[
        {
            "role": "user",
            "content": "O que é IA?"
        }
    ],
    temperature=1,                    # criatividade (0 a 2)
    max_completion_tokens=7000,       # limite de tokens na resposta
    reasoning_effort="medium",        # esforço de raciocínio
    stream=True,                      # resposta em tempo real
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
```

### O parâmetro `temperature`

| Valor | Comportamento |
|---|---|
| `0` | Determinístico — sempre escolhe a opção mais provável |
| `0.5` | Balanceado |
| `1` | Criativo — mais variação nas respostas |
| `2` | Muito criativo — pode ser menos preciso |

**Regra prática:** use temperatura baixa para código e dados, alta para texto criativo.

### `stream=True` — resposta em tempo real

Com `stream=True`, a resposta chega em pedaços (`chunks`) à medida que é gerada, como você vê no ChatGPT. Por isso o loop `for chunk in completion`.

---

## 7. Lista de Dicionários — Estrutura Real de Dados

Quando você precisa associar múltiplas informações a cada item:

```python
# ❌ Problema com listas separadas — fácil de desincronizar
lista_de_nomes  = ["Maria Silva", "João Santos", "Ana Oliveira"]
lista_de_medias = [8.9, 7.5, 4.2]

# ✅ Solução com lista de dicionários
alunos = [
    {"nome": "Maria Silva",  "media": 8.9},
    {"nome": "João Santos",  "media": 7.5},
    {"nome": "Ana Oliveira", "media": 4.2},
    {"nome": "Pedro Costa",  "media": 1.4},
]
```

### Acessando elementos

```python
alunos[0]               # {'nome': 'Maria Silva', 'media': 8.9}
alunos[0]["nome"]       # 'Maria Silva'
alunos[0]["media"]      # 8.9

# Iterando
for aluno in alunos:
    print(f"{aluno['nome']}: {aluno['media']}")
```

### Por que isso é melhor que duas listas separadas?

Com listas separadas, se você adicionar um nome sem adicionar a média correspondente, tudo fica fora de sincronia. Com lista de dicionários, nome e média ficam sempre juntos no mesmo objeto — impossível de dissociar por acidente.

---

## 8. Dicionários — Revisão Rápida

```python
# Criar
dados = {
    "Maria Silva": 8.9,
    "João Santos": 7.5,
}

# Acessar
dados["Maria Silva"]          # 8.9
dados.get("Maria Silva")      # 8.9 (sem erro se não existir)

# Métodos de consulta
dados.keys()    # dict_keys(['Maria Silva', 'João Santos'])
dados.values()  # dict_values([8.9, 7.5])
dados.items()   # dict_items([('Maria Silva', 8.9), ('João Santos', 7.5)])

# Remover
dados.pop("Maria Silva")
```

---

## 9. Resumo Rápido

| O que fazer | Como fazer |
|---|---|
| Pergunta simples ao Gemini | `client.models.generate_content(model=..., contents=...)` |
| Chat com histórico | `chat = client.chats.create(model=...)` + `chat.send_message(...)` |
| Ver histórico do chat | `chat.get_history()` |
| Loop de chatbot | `while prompt != "fim":` |
| Resumidor com numeração | `for numero, item in enumerate(lista):` |
| Usar modelo open source | Groq API + `client.chat.completions.create(...)` |
| Controlar criatividade | `temperature=` (0 = preciso, 2 = criativo) |
| Lista de dicionários | `[{"chave": valor}, {"chave": valor}]` |
| Acessar na lista de dict | `lista[0]["chave"]` |
