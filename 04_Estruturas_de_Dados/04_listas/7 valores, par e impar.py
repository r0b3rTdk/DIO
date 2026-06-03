numeros = [[], []]

for i in range(0, 7):
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

numeros[0].sort()
numeros[1].sort()

print(f"Números digitados: {numeros}")
print(f"Números pares: {numeros[0]}")
print(f"Números ímpares: {numeros[1]}")