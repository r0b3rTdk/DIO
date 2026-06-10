# 🐍 Python & POO — Guia Direto de Herança

> Sem enrolação — só o que importa na prática

---

## 1. O que é Herança?

Herança é um mecanismo onde uma classe filha herda automaticamente todos os atributos e métodos de outra classe pai. É literalmente reutilização de código.

> **Analogia:** Classe pai = Animal. Classe filha = Cachorro. O Cachorro herda tudo de Animal e ainda pode ter coisas suas.

**Sintaxe básica:**
```python
class Pai:
    pass

class Filho(Pai):   # Filho herda tudo de Pai
    pass
```

---

## 2. Herança Simples

Uma classe filha, um pai. O caso mais comum.

### 2.1 Filho que só herda (sem mudança)

Se o filho não precisa de nada a mais, só usa `pass`:

```python
class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

class Motocicleta(Veiculo):
    pass   # herda tudo — cor, placa, rodas, ligar_motor()

class Carro(Veiculo):
    pass   # idem

moto = Motocicleta("preta", "abc-1234", 2)
moto.ligar_motor()   # Funciona! Herdou do Veiculo
```

> **Por que?** Moto e Carro são veículos — faz sentido herdar cor, placa e `ligar_motor()`. Não precisa reescrever.

---

### 2.2 Filho que adiciona atributo extra

Quando o filho precisa de atributo próprio, você cria `__init__` no filho e usa `super()` para inicializar o pai:

```python
class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)  # inicializa o pai
        self.carregado = carregado                  # atributo exclusivo

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Nao'} estou carregado")

caminhao = Caminhao("roxo", "gfd-8712", 8, True)
caminhao.esta_carregado()  # Sim estou carregado
caminhao.ligar_motor()     # herdou do Veiculo
```

> ⚠️ **`super()`:** `super().__init__(...)` chama o `__init__` do pai. Sem ele, os atributos do pai (cor, placa, rodas) nunca seriam criados e quebra.

---

## 3. Herança Múltipla

Uma classe filha herda de dois ou mais pais ao mesmo tempo. Útil quando uma entidade tem características de várias categorias.

### 3.1 Exemplo: Ornitorrinco

O ornitorrinco é mamífero E ave — herança múltipla faz sentido aqui:

```python
class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)      # passa o resto pra frente

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)      # passa o resto pra frente

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        super().__init__(
            cor_pelo=cor_pelo,
            cor_bico=cor_bico,
            nro_patas=nro_patas
        )

o = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(o.cor_pelo)    # vermelho
print(o.cor_bico)    # laranja
print(o.nro_patas)   # 2
```

---

## 4. O que é `**kw` (kwargs)?

Esse é o ponto que mais confunde em herança múltipla. Entender `**kw` muda tudo.

### 4.1 O problema SEM `**kw`

```python
# SEM **kw — QUEBRA em herança múltipla
class Mamifero(Animal):
    def __init__(self, cor_pelo, nro_patas):  # nro_patas fica preso aqui
        self.cor_pelo = cor_pelo
        super().__init__(nro_patas)

class Ave(Animal):
    def __init__(self, cor_bico, nro_patas):  # nro_patas fica preso aqui também
        self.cor_bico = cor_bico
        super().__init__(nro_patas)

# Ornitorrinco herda de Mamifero E Ave
# Como passar nro_patas para os dois? Impossível sem **kw → TypeError
```

### 4.2 A solução: `**kw`

`**kw` captura todos os argumentos que a classe não precisa e passa adiante via `super()`:

```python
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):   # **kw = "o resto dos argumentos"
        self.cor_pelo = cor_pelo
        super().__init__(**kw)             # repassa o resto (nro_patas, cor_bico...)

# Fluxo quando Ornitorrinco é criado com (cor_pelo="X", cor_bico="Y", nro_patas=2):
# 1. Mamifero pega cor_pelo → kw = {cor_bico="Y", nro_patas=2}
# 2. Ave pega cor_bico     → kw = {nro_patas=2}
# 3. Animal pega nro_patas → chegou!
```

> 💡 **Resumo:** `**kw` = "pega o que sobrou e passa pra frente". Sem ele, herança múltipla com `__init__` quebra.

---

## 5. MRO — A Ordem que o Python Segue

MRO (Method Resolution Order) é a ordem que o Python usa para procurar métodos e atributos quando há herança. Sempre da esquerda para a direita, de baixo para cima.

```python
class Ornitorrinco(Mamifero, Ave):
    pass

print(Ornitorrinco.__mro__)
# (<class 'Ornitorrinco'>, <class 'Mamifero'>, <class 'Ave'>, <class 'Animal'>, <class 'object'>)
```

A ordem de busca é:
1. `Ornitorrinco`
2. `Mamifero` (primeiro da esquerda)
3. `Ave` (segundo da esquerda)
4. `Animal` (pai comum)
5. `object` (pai de tudo em Python)

> ⚠️ **Por que importa?** O `super()` não chama necessariamente o pai direto — ele segue o MRO. Entender isso evita bugs obscuros em herança múltipla.

---

## 6. Sobrescrita de Métodos (Override)

Você pode redefinir um método do pai no filho. O filho usa a versão dele, não a do pai.

```python
class Animal:
    def falar(self):
        print("...")

class Cachorro(Animal):
    def falar(self):         # sobrescreve o falar do Animal
        print("Au au!")

class Gato(Animal):
    def falar(self):
        print("Miau!")

c = Cachorro()
c.falar()   # Au au! — usa o do Cachorro, não do Animal

# Quer usar o do pai E adicionar algo? Usa super():
class Cachorro(Animal):
    def falar(self):
        super().falar()      # chama o do Animal primeiro
        print("Au au!")
```

---

## 7. Referência Rápida

| Situação | O que fazer |
|---|---|
| Filho sem atributo extra | Não cria `__init__` — herda o do pai automaticamente |
| Filho com atributo extra | Cria `__init__` e usa `super().__init__(...)` |
| Herança múltipla com `__init__` | Usa `**kw` em cada `__init__` intermediário |
| Ver a ordem de busca | `Classe.__mro__` |
| Redefinir método do pai | Reescreve o método no filho (override) |
| Usar o método do pai + algo extra | `super().metodo()` dentro do override |

---

## 8. Exemplo Completo Comentado

```python
class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        # mostra o nome real da classe + todos os atributos
        attrs = ', '.join(f'{k}={v}' for k, v in self.__dict__.items())
        return f'{self.__class__.__name__}: {attrs}'


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):  # **kw = argumentos que não são meus
        self.cor_pelo = cor_pelo
        super().__init__(**kw)            # repassa o restante pro próximo na MRO


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero):   # herda de Mamifero que herda de Animal
    pass                 # sem __init__ próprio — usa o de Mamifero


class Ornitorrinco(Mamifero, Ave):   # herda dos dois
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        super().__init__(
            cor_pelo=cor_pelo,   # vai pra Mamifero
            cor_bico=cor_bico,   # vai pra Ave
            nro_patas=nro_patas  # vai pra Animal
        )


gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)
# Gato: cor_pelo=Preto, nro_patas=4

o = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(o)
# Ornitorrinco: cor_pelo=vermelho, cor_bico=laranja, nro_patas=2

print(Ornitorrinco.__mro__)
# Ornitorrinco -> Mamifero -> Ave -> Animal -> object
```
