valores = []

for i in range(1, 6):
    valores.append(int(input(f"digite o {i} numero: ")))

print(valores)

maior_valor = max(valores)
menor_valor = min(valores)

print(f"\no menor numero foi o {min(valores)} no indice: ", end=' ')    
for i, v in enumerate(valores):
    if v == menor_valor:    
        print(f".{i}.", end= '')

print(f"\no maior numero foi o {max(valores)} no indice: ", end=' ')    
for i, v in enumerate(valores):
    if v == maior_valor:
        print(f".{i}.", end='')
