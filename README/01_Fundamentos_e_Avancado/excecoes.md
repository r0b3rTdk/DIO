# 🛡️ Tratamento de Exceções em Python — Guia Completo

> Criar fluxos alternativos quando algo dá errado — sem deixar o programa morrer

---

## 1. O que são Exceções?

Exceção = erro que acontece **durante a execução**. Sem tratamento, o programa para completamente.

O objetivo é criar um **fluxo alternativo**: o programa não quebra, mas avisa o usuário do problema de forma clara.

---

## 2. Estrutura Completa

```python
try:
    # código que pode falhar
except TipoDeErro:
    # trata esse erro específico
except OutroErro as e:
    # trata outro tipo, capturando a mensagem
else:
    # executado SÓ se não houve erro
finally:
    # executado SEMPRE — com ou sem erro
```

| Cláusula | Quando roda |
|---|---|
| `try` | Sempre — é o fluxo principal |
| `except` | Só se ocorreu um erro no `try` |
| `else` | Só se o `try` completou **sem** erros |
| `finally` | **Sempre** — com ou sem erro |

---

## 3. Try / Except

```python
notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0]}

try:
    nome = input("Digite o nome: ")
    resultado = notas[nome]
except KeyError:
    print("Estudante não matriculado(a) na turma")
```

### Capturando o erro como variável

```python
except Exception as e:
    print(type(e), f"Erro: {e}")
# <class 'KeyError'> Erro: 'Mirla'
```

Útil pra mostrar o erro sem expor a mensagem técnica completa do Python.

---

## 4. Else

Roda **somente se o `try` completou sem erros**:

```python
try:
    resultado = notas[nome]
except KeyError:
    print("Estudante não encontrado")
else:
    print(resultado)   # só chega aqui se não houve erro
```

---

## 5. Finally

Roda **sempre** — com ou sem erro. Usado pra mensagens de encerramento, fechar arquivos, fechar conexão com banco.

```python
try:
    resultado = notas[nome]
except KeyError:
    print("Estudante não encontrado")
else:
    print(resultado)
finally:
    print("Consulta encerrada!")   # sempre roda
```

---

## 6. Raise — Lançando Exceção Manualmente

`raise` cria um erro quando algo **não é tecnicamente errado pra linguagem, mas é errado pro seu programa**.

```python
def media(lista):
    calculo = sum(lista) / len(lista)

    if len(lista) > 4:
        raise ValueError("A lista não pode possuir mais de 4 notas.")

    return calculo
```

---

## 7. Múltiplos Except

```python
try:
    notas = [6, 7, 8, 9]
    resultado = media(notas)

except TypeError:
    print("Só são aceitos valores numéricos!")

except ValueError as e:
    print(e)   # imprime a mensagem do raise

else:
    print(resultado)

finally:
    print("Consulta encerrada!")
```

### Os 3 cenários:

```python
# Lista válida → 7.5 / Consulta encerrada!
# Mais de 4 notas → A lista não pode possuir mais de 4 notas. / Consulta encerrada!
# Valor não numérico → Só são aceitos valores numéricos! / Consulta encerrada!
```

> ⚠️ A hierarquia importa: o Python executa o código na ordem. Se `sum()` rodar antes do `if len()`, o `TypeError` aparece antes do `ValueError`.

---

## 8. Tipos de Erro mais Comuns

| Erro | Quando acontece | Exemplo |
|---|---|---|
| `KeyError` | Chave não existe no dicionário | `d["chave_errada"]` |
| `TypeError` | Tipo de dado errado pra operação | `sum([1, 2, "3"])` |
| `ValueError` | Valor inválido pro contexto | `int("abc")` |
| `ZeroDivisionError` | Divisão por zero | `10 / 0` |
| `IndexError` | Índice fora do range | `lista[999]` |
| `FileNotFoundError` | Arquivo não existe | `open("nao_existe.txt")` |

---

## 9. Fluxo Visual

```
        try
         │
    ┌────▼────┐
    │ código  │
    └────┬────┘
         │
    erro?├──── SIM ──► except → trata o erro
         │
        NÃO
         │
        else → usa o resultado
         │
      (sempre)
         │
       finally → encerramento / fechar recursos
```

---

## 10. Regra de Ouro

> Nunca use `except:` sem especificar o tipo de erro.
> Isso captura qualquer erro silenciosamente e esconde bugs reais.

```python
# ❌ Ruim — captura tudo e esconde bugs
except:
    pass

# ✅ Certo — específico e claro
except KeyError:
    print("Chave não encontrada")

except (TypeError, ValueError) as e:   # também dá pra agrupar numa tupla
    print(f"Erro de tipo ou valor: {e}")
```
