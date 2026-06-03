import random

def sorteia(lista):
    for i in range(6):
        numero = random.randint(1, 60)
        lista.append(numero)
    print(f"os numeros sorteados foram: {lista}")

def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f"A soma dos números pares é: {soma}")

numeros = []
sorteia(numeros)
somaPar(numeros)
