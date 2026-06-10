# 🛡️ Tratamento de Erros e Depuração em Python

> Código que não quebra em produção — o que separa júnior de pleno

---

## 1. O que são Exceções?

Exceção = um erro que acontece **durante a execução** do programa.
Quando acontece sem tratamento, o programa para completamente.

```python
numero = 10 / 0   # ZeroDivisionError — programa morre aqui
print("isso nunca vai aparecer")
```

O objetivo do tratamento de erros é **evitar que o programa pare** e dar uma resposta útil.

---

## 2. Tipos de Erro mais Comuns

| Erro | Quando acontece | Exemplo |
|---|---|---|
| `SyntaxError` | Código mal escrito — Python nem roda | `if x = 1:` |
| `TypeError` | Operação com tipo errado | `"texto" + 10` |
| `ValueError` | Valor inválido pro que foi pedido | `int("abc")` |
| `ZeroDivisionError` | Divisão por zero | `10 / 0` |
| `FileNotFoundError` | Arquivo não existe | `open("nao_existe.txt")` |
| `KeyError` | Chave não existe no dicionário | `d["chave_errada"]` |
| `IndexError` | Índice fora do range da lista | `lista[999]` |

> 📖 Lista completa: https://docs.python.org/pt-br/3/tutorial/errors.html

---

## 3. Try / Except — O Básico

### Estrutura

```python
try:
    # código que pode dar erro
except TipoDoErro:
    # o que fazer SE der esse erro
```

### Exemplo

```python
try:
    numero = 10 / 0
    print(numero)

except ZeroDivisionError:
    print("Erro: divisão por zero.")

# programa continua normalmente aqui — não morreu
```

### Capturando múltiplos erros

```python
try:
    numero = int(input("Digite um número: "))
    print(10 / numero)

except ZeroDivisionError:
    print("Não é possível dividir por zero.")

except ValueError:
    print("Digite apenas números.")
```

Cada `except` trata um tipo de erro diferente. O Python cai no primeiro que bater.

### Capturando o erro como variável

```python
try:
    numero = int("abc")

except ValueError as erro:
    print(f"Ocorreu um erro: {erro}")
    # Ocorreu um erro: invalid literal for int() with base 10: 'abc'
```

Útil pra logar o erro ou exibir a mensagem original.

---

## 4. Finally — Executa Sempre

`finally` roda **independente de ter dado erro ou não**.
Muito usado pra fechar conexões, arquivos, limpar recursos.

```python
try:
    numero = int("10")
    print(numero)

except ValueError:
    print("Erro de conversão")

finally:
    print("Execução finalizada")   # sempre roda — com ou sem erro
```

**Caso com erro:**
```
Erro de conversão
Execução finalizada
```

**Caso sem erro:**
```
10
Execução finalizada
```

> 💡 Com arquivos e banco de dados, o `finally` garante que a conexão
> sempre será fechada, mesmo se algo quebrar no meio.

---

## 5. Raise — Gerando Erro Manualmente

`raise` permite que **você** lance um erro quando uma regra de negócio é violada.

```python
idade = -5

if idade < 0:
    raise ValueError("Idade não pode ser negativa")
```

**Por que usar?** Porque às vezes o Python não sabe que aquilo é um erro —
só você sabe. O `raise` formaliza isso.

```python
def calcular_raiz(numero):
    if numero < 0:
        raise ValueError("Não existe raiz de número negativo")
    return numero ** 0.5

calcular_raiz(-4)   # ValueError: Não existe raiz de número negativo
```

---

## 6. Prevenção — Melhor que Remediar

Quando possível, **verifique antes** de tentar executar:

```python
# ruim — espera dar erro pra tratar
try:
    numero = int(entrada)
except:
    ...

# melhor — verifica antes
entrada = input("Digite um número: ")

if entrada.isdigit():
    numero = int(entrada)
    print(numero)
else:
    print("Valor inválido")
```

---

## 7. Depuração (Debugging)

Depurar = encontrar e corrigir erros no código.

### Print Debugging — o mais simples

Coloca `print()` estratégicos pra acompanhar o fluxo e ver os valores:

```python
numero = 10
divisor = 0

print("numero:", numero)     # confirma o valor
print("divisor:", divisor)   # vê que é 0 antes do erro

resultado = numero / divisor   # aí descobre o problema
```

### Lendo o Stack Trace

Quando o Python joga um erro, ele mostra o **stack trace** — o caminho que o código percorreu até chegar no erro:

```python
def dividir(a, b):
    return a / b

dividir(10, 0)
```

```
ZeroDivisionError: division by zero
  File "script.py", line 4, in <module>
    dividir(10, 0)          ← chamou aqui
  File "script.py", line 2, in dividir
    return a / b            ← quebrou aqui
```

**Como ler:** leia de baixo pra cima. A última linha é onde o erro aconteceu.
As linhas acima mostram o caminho até chegar lá.

---

## 8. Logging — O Print Profissional

Em projetos reais, `print()` temporário não escala. O `logging` registra eventos
de forma estruturada, com nível de severidade e pode salvar em arquivo.

### Níveis disponíveis

| Nível | Quando usar |
|---|---|
| `DEBUG` | Detalhes internos — só durante desenvolvimento |
| `INFO` | Eventos normais — "processo iniciado", "arquivo salvo" |
| `WARNING` | Algo suspeito, mas não quebrou ainda |
| `ERROR` | Erro aconteceu, mas o programa continua |
| `CRITICAL` | Erro grave — sistema pode estar comprometido |

### Usando na prática

```python
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Mensagem de debug")     # detalhes internos
logging.info("Informação geral")       # evento normal
logging.warning("Aviso")              # algo suspeito
logging.error("Erro ocorrido")        # erro real
```

> 💡 `basicConfig(level=logging.DEBUG)` define o nível mínimo a exibir.
> Em produção você usaria `INFO` ou `WARNING` — não quer logar tudo.

### Salvando log em arquivo

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="app.log",           # salva em arquivo
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Programa iniciado")
logging.error("Falha ao conectar ao banco")
```

O arquivo `app.log` vai ter:
```
2024-01-15 10:30:00 - INFO - Programa iniciado
2024-01-15 10:30:01 - ERROR - Falha ao conectar ao banco
```

---

## 9. Exemplo Completo — Tudo junto

```python
import logging

logging.basicConfig(level=logging.INFO)

def dividir(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Os valores precisam ser números")   # raise

    if b == 0:
        raise ValueError("Divisor não pode ser zero")        # raise

    return a / b


def calcular_com_seguranca(a, b):
    try:
        resultado = dividir(a, b)
        logging.info(f"Cálculo realizado: {a} / {b} = {resultado}")
        return resultado

    except TypeError as e:
        logging.error(f"Tipo inválido: {e}")
        return None

    except ValueError as e:
        logging.warning(f"Valor inválido: {e}")
        return None

    finally:
        logging.debug("Tentativa de cálculo finalizada")   # sempre roda


print(calcular_com_seguranca(10, 2))    # 5.0
print(calcular_com_seguranca(10, 0))    # None — aviso no log
print(calcular_com_seguranca("a", 2))   # None — erro no log
```

---

## 10. Resumo Rápido

```python
try:
    # tenta executar
except TipoErro:
    # trata o erro específico
except OutroErro as e:
    # captura o erro como variável
finally:
    # sempre executa — com ou sem erro

raise ValueError("mensagem")   # lança erro manualmente
```

**Regras práticas:**
- Sempre especifique o tipo do erro no `except` — nunca use `except:` sozinho (pega tudo, esconde bugs)
- Use `raise` pra validar regras de negócio que o Python não conhece
- Use `logging` em vez de `print()` em código que vai pra produção
- Leia o stack trace de baixo pra cima — a última linha é onde quebrou
