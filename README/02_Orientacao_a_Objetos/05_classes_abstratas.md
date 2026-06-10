# 📋 Classes Abstratas e Interfaces em Python

> Definir o que uma classe deve fazer — sem dizer como

---

## 1. O que é uma Interface?

Interface é um **contrato**: define quais métodos uma classe é obrigada a ter,
mas não implementa nenhum deles. Quem assina o contrato (a classe filha) que
decide como cada método funciona.

```
Interface diz:  "você DEVE ter ligar() e desligar()"
Classe filha:   "ok, aqui está meu ligar() e meu desligar()"
```

> Python não tem a palavra `interface` como Java ou C#.
> A solução é usar **classes abstratas com ABC**.

---

## 2. O que é ABC?

`ABC` é um módulo do Python que permite criar classes abstratas.
Uma classe abstrata é aquela que:

- Define métodos que as filhas **são obrigadas** a implementar
- **Não pode ser instanciada diretamente** — só existe pra servir de base
- Funciona como a "interface" do Python

```python
from abc import ABC, abstractmethod
```

---

## 3. O Problema sem Classes Abstratas

```python
class ControleRemoto:
    def ligar(self):
        pass

class ControleTV(ControleRemoto):
    pass   # esqueceu de implementar ligar() — Python não avisa!

c = ControleTV()
c.ligar()   # não faz nada, sem erro — bug silencioso
```

Com classe abstrata, o Python avisa na hora certa:

```python
from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

class ControleTV(ControleRemoto):
    pass   # esqueceu ligar()

c = ControleTV()   # → TypeError: não pode instanciar, falta implementar ligar()
```

---

## 4. Como Funciona na Prática

```python
from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):         # herda de ABC → vira classe abstrata

    @abstractmethod
    def ligar(self):               # obrigado a implementar nas filhas
        pass

    @abstractmethod
    def desligar(self):            # obrigado a implementar nas filhas
        pass

    @property
    @abstractproperty
    def marca(self):               # propriedade obrigatória nas filhas
        pass
```

Agora as classes filhas **precisam implementar tudo** ou Python joga erro:

```python
class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"
```

```python
controle = ControleTV()
controle.ligar()          # Ligando a TV... / Ligada!
controle.desligar()       # Desligando a TV... / Desligada!
print(controle.marca)     # Philco

controle = ControleArCondicionado()
controle.ligar()          # Ligando o Ar Condicionado... / Ligado!
controle.desligar()       # Desligando o Ar Condicionado... / Desligado!
print(controle.marca)     # LG
```

---

## 5. `@abstractmethod` vs `@abstractproperty`

| Decorador | Serve pra | Exemplo |
|---|---|---|
| `@abstractmethod` | Métodos normais obrigatórios | `ligar()`, `desligar()` |
| `@property` + `@abstractproperty` | Propriedades obrigatórias | `marca` |

> ⚠️ `abstractproperty` está **depreciado** nas versões mais novas do Python.
> O jeito moderno é usar só `@property` + `@abstractmethod` juntos:

```python
# jeito moderno (preferido)
@property
@abstractmethod
def marca(self):
    pass
```

---

## 6. Regras Importantes

```python
# 1. Classe abstrata NÃO pode ser instanciada
c = ControleRemoto()   # → TypeError

# 2. Filha que não implementar TUDO não pode ser instanciada
class ControleIncompleto(ControleRemoto):
    def ligar(self):    # implementou só ligar()
        pass

c = ControleIncompleto()   # → TypeError: falta desligar() e marca

# 3. Filha que implementar tudo funciona normalmente
c = ControleTV()   # funciona
```

---

## 7. Quando Usar Classe Abstrata?

Use quando a **classe base não faz sentido existir sozinha** e você quer garantir
que toda filha siga um padrão.

| Situação | Usa ABC? |
|---|---|
| `ControleRemoto` → `ControleTV`, `ControleAr` (controle genérico não existe) | ✅ Sim |
| `Forma` → `Circulo`, `Retangulo` (forma genérica não existe) | ✅ Sim |
| `Animal` → `Cachorro`, `Gato` (animal genérico não faz nada) | ✅ Sim |
| Classe simples sem hierarquia obrigatória | ❌ Não precisa |

---

## 8. Resumo Rápido

```python
from abc import ABC, abstractmethod

class MinhaInterface(ABC):      # 1. herda de ABC

    @abstractmethod
    def metodo_obrigatorio(self):   # 2. decora com @abstractmethod
        pass                         #    corpo fica vazio (pass)

class MinhaClasse(MinhaInterface):
    def metodo_obrigatorio(self):   # 3. filha implementa de verdade
        print("Implementado!")

# MinhaInterface()   → erro
# MinhaClasse()      → funciona
```

> 💡 **Resumo de uma linha:** ABC define o **contrato** ("o que fazer"),
> as filhas definem a **implementação** ("como fazer").
