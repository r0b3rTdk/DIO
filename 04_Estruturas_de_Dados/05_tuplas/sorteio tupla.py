import random

numeros = (
    random.randint(0, 10),
    random.randint(0, 10),  
    random.randint(0, 10),  
    random.randint(0, 10),
    random.randint(0, 10)  
)

print(numeros)
maior_valor = max(numeros)
print(f"O maior valor na tupla é: {maior_valor}")
menor_valor = min(numeros)
print(f"O menor valor na tupla é: {menor_valor}")
