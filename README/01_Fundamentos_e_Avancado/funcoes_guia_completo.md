# 🐍 Funções em Python — Guia Completo

> Bibliotecas, funções, lambda, map, filter e zip — tudo que você precisa saber

---

## 1. Bibliotecas e Importações

### Formas de importar

```python
import math                        # importa a biblioteca inteira
import matplotlib.pyplot as plt    # importa com apelido (alias)
from random import choice          # importa só um método
from random import randrange, sample  # importa vários métodos
from math import *                 # importa tudo (cuidado com conflitos)
```

**Quando usar cada uma:**

| Forma | Quando usar |
|---|---|
| `import lib` | Quando vai usar vários métodos da biblioteca |
| `import lib as apelido` | Convenção consagrada (np, pd, plt) |
| `from lib import metodo` | Quando usa só 1 ou 2 métodos específicos |
| `from lib import *` | Evite — pode causar conflito de nomes |

> 💡 `help(funcao)` mostra a documentação de qualquer método — útil quando não sabe os parâmetros.

### Pip — Gerenciador de pacotes

```bash
!pip list                   # lista todos os pacotes instalados
!pip install nome_pacote    # instala um pacote
```

---

## 2. Funções Built-in (Embutidas)

Funções que já existem no Python, sem precisar importar nada:

```python
print()     # exibe no terminal
len()       # tamanho de listas, strings, dicionários
sum()       # soma de uma lista
round()     # arredondamento
type()      # tipo da variável
list()      # converte para lista
help()      # mostra a documentação
input()     # lê entrada do usuário
```

```python
notas = [8.5, 9.0, 7.0]

soma = sum(notas)            # 24.5
quantidade = len(notas)      # 3
media = soma / quantidade    # 8.166...
media_arredondada = round(media, 1)   # 8.2
```

---

## 3. Criando Funções Próprias

### Sem parâmetros

```python
def saudacao():
    print("Olá, mundo!")

saudacao()   # Olá, mundo!
```

### Com parâmetros

```python
def media(nota_1, nota_2, nota_3):
    calculo = (nota_1 + nota_2 + nota_3) / 3
    print(calculo)

media(8, 9, 7)   # 8.0
```

> **Parâmetros** → nomes definidos na criação da função (`nota_1, nota_2, nota_3`)
> **Argumentos** → valores passados na chamada da função (`8, 9, 7`)

### Com `return` — retornando valores

Sem `return`, a função retorna `None` — você não consegue salvar o resultado em variável.

```python
def media(lista):
    calculo = sum(lista) / len(lista)
    return calculo          # ← agora o valor sai da função

notas = [8.5, 9.0, 6.0, 10.0]
resultado = media(notas)   # 8.375
print(resultado)           # funciona!
```

### Retornando múltiplos valores (tupla)

```python
def boletim(lista):
    media = sum(lista) / len(lista)

    if media >= 6:
        situacao = "Aprovado(a)"
    else:
        situacao = "Reprovado(a)"

    return (media, situacao)   # retorna uma tupla

media, situacao = boletim([8.5, 9.0, 6.0, 5.0])
print(f"Média: {media}, Situação: {situacao}")
# Média: 7.125, Situação: Aprovado(a)
```

---

## 4. Escopo de Função

Variável criada dentro de uma função **só existe dentro dela**. Isso se chama **escopo**.

```python
def calcular():
    resultado = 42    # existe só aqui dentro
    return resultado

print(resultado)   # NameError! resultado não existe aqui fora
```

Por isso o `return` é essencial — é a única forma de tirar um valor de dentro da função.

---

## 5. Type Hint e Default Value

Boas práticas pra deixar o código mais legível e documentado:

```python
# Type Hint: indica o tipo esperado dos parâmetros e do retorno
def media(lista: list) -> float:
    return sum(lista) / len(lista)

# Default Value: valor padrão caso nenhum argumento seja passado
def media(lista: list = [0]) -> float:
    return sum(lista) / len(lista)

media()      # 0.0  — usou o valor padrão
media([8, 9, 7])   # 8.0
```

---

## 6. Docstring — Documentando funções

```python
def media(lista: list = [0]) -> float:
    '''Calcula a média dos valores de uma lista.

    lista: list, default [0]
        Lista com os valores para calcular a média.
    return: float
        Média calculada.
    '''
    return sum(lista) / len(lista)

help(media)   # exibe a documentação que você escreveu
```

---

## 7. Função Lambda — Função Anônima

Lambda é uma função sem nome, escrita em uma linha. Ideal para operações simples e rápidas.

```python
# Função normal
def qualitativo(x):
    return x + 0.5

# Equivalente em lambda
qualitativo = lambda x: x + 0.5

qualitativo(8)   # 8.5
```

### Lambda com múltiplos parâmetros

```python
media_ponderada = lambda x, y, z: (x * 3 + y * 2 + z * 5) / 10

media_ponderada(8, 5, 9)   # 7.9
```

---

## 8. `map()` — Transformar Listas

`map()` aplica uma função a **cada elemento** de uma lista. A lista final tem o **mesmo tamanho** da original.

```python
notas = [6.0, 7.0, 9.0, 5.5, 8.0]
qualitativo = 0.5

# Adiciona 0.5 em cada nota
notas_atualizadas = list(map(lambda x: x + qualitativo, notas))
print(notas_atualizadas)
# [6.5, 7.5, 9.5, 6.0, 8.5]
```

> ⚠️ O `map()` retorna um objeto especial — use `list()` pra ver o resultado.

---

## 9. `filter()` — Filtrar Listas

`filter()` aplica um teste lógico a cada elemento e **só mantém os que passaram** (`True`). A lista final pode ser menor que a original.

```python
idades = [15, 22, 17, 30, 45, 12, 18]

# Mantém só os maiores de idade
permitidos = list(filter(lambda idade: idade >= 18, idades))
print(permitidos)
# [22, 30, 45, 18]
```

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Mantém só os pares
pares = list(filter(lambda n: n % 2 == 0, numeros))
print(pares)
# [2, 4, 6, 8, 10]
```

### `map()` vs `filter()` — Nunca mais confundir

| | `map()` | `filter()` |
|---|---|---|
| O que faz | **Modifica** cada item | **Seleciona** itens por uma condição |
| Tamanho da lista final | Mesmo tamanho | Menor ou igual |
| A função deve retornar | O valor transformado | `True` ou `False` |
| Exemplo | Dar 10% de desconto em todos os preços | Mostrar só produtos abaixo de R$50 |

```python
precos = [30, 80, 45, 120, 15]

# map: aplica desconto de 10% em TODOS
com_desconto = list(map(lambda p: p * 0.9, precos))
# [27.0, 72.0, 40.5, 108.0, 13.5]

# filter: seleciona só os que custam menos de R$50
baratos = list(filter(lambda p: p < 50, precos))
# [30, 45, 15]
```

---

## 10. `zip()` — Juntando Listas

`zip()` funciona como um zíper: junta o elemento de posição 0 de uma lista com o de posição 0 da outra, depois posição 1 com 1, e assim por diante.

### Básico: juntando duas listas

```python
nomes = ["Ana", "Bruno", "Carlos"]
idades = [25, 30, 22]

pares = list(zip(nomes, idades))
print(pares)
# [('Ana', 25), ('Bruno', 30), ('Carlos', 22)]
```

### Regra do mais curto — listas de tamanhos diferentes

Se uma lista for maior, o `zip()` para quando a menor acabar:

```python
jogadores = ["Pelé", "Maradona", "Messi", "Zidane"]
camisas = [10, 10, 10]   # só 3 itens

pares = list(zip(jogadores, camisas))
print(pares)
# [('Pelé', 10), ('Maradona', 10), ('Messi', 10)]
# Zidane foi ignorado — não tinha par
```

### Zippando 3 ou mais listas

```python
nomes = ["João", "Maria"]
sobrenomes = ["Silva", "Souza"]
idades = [20, 25]

for n, s, i in zip(nomes, sobrenomes, idades):
    print(f"{n} {s} tem {i} anos.")
# João Silva tem 20 anos.
# Maria Souza tem 25 anos.
```

### Criando dicionários com `zip` + `dict`

```python
chaves = ["nome", "idade", "cidade"]
valores = ["Diana", 28, "Bayeux"]

dicionario = dict(zip(chaves, valores))
print(dicionario)
# {'nome': 'Diana', 'idade': 28, 'cidade': 'Bayeux'}
```

Muito usado em ciência de dados quando você tem uma lista de colunas e uma lista de valores.

### Desfazendo o zip — Unzip

```python
pares = [('Ana', 25), ('Bruno', 30), ('Carlos', 22)]

nomes, idades = zip(*pares)   # * desempacota

print(nomes)    # ('Ana', 'Bruno', 'Carlos')
print(idades)   # (25, 30, 22)
```

---

## 11. Exemplo Completo — Tudo junto

```python
from random import sample

# Dados
nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]
notas = [8.5, 6.0, 9.5, 5.5, 7.0]

# Junta nome com nota
turma = dict(zip(nomes, notas))

# Filtra aprovados (nota >= 6)
aprovados = {nome: nota for nome, nota in turma.items() if nota >= 6}

# Adiciona 0.5 de qualitativo nos aprovados
com_bonus = {nome: nota + 0.5 for nome, nota in aprovados.items()}

# Função com type hint e docstring
def resumo(dicionario: dict) -> None:
    '''Exibe o resumo de notas de uma turma.

    dicionario: dict
        Dicionário com {nome: nota}
    '''
    for nome, nota in dicionario.items():
        print(f"{nome}: {nota:.1f}")

resumo(com_bonus)
# Ana: 9.0
# Bruno: 6.5
# Carlos: 10.0
# Eduardo: 7.5
```

---

## 12. Resumo Rápido

| Conceito | Sintaxe | Serve pra |
|---|---|---|
| Função simples | `def nome(param): return valor` | Reutilizar lógica |
| Type Hint | `def f(x: int) -> float:` | Documentar tipos esperados |
| Default Value | `def f(x: int = 0):` | Valor padrão se não passar argumento |
| Docstring | `'''texto'''` dentro da função | Documentar o que a função faz |
| Lambda | `lambda x: expressao` | Função rápida de uma linha |
| `map()` | `list(map(lambda x: ..., lista))` | Transformar todos os elementos |
| `filter()` | `list(filter(lambda x: ..., lista))` | Selecionar elementos por condição |
| `zip()` | `list(zip(lista1, lista2))` | Juntar listas em pares |
| `dict(zip())` | `dict(zip(chaves, valores))` | Criar dicionário de duas listas |
| `zip(*lista)` | `a, b = zip(*pares)` | Separar lista de pares em listas independentes |
