matriz = [[0, 0 ,0], [0, 0, 0], [0, 0, 0]]
spar = mai = scoluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"digite o numero da {l}/{c}: "))

print('-'*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-'*20)
print(f"a soma dos valores pares foi: {spar}")
for l in range(0, 3):
    scoluna += matriz[l][2]
print(f"a soma dos valores da 3 coluna: {scoluna}")
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f"o maior numero da linha do meio foi: {mai}")