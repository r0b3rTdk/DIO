l1 = [1, 2, 4, 5, 8, 9]
l2 = [3, 5, 7, 9, 1]
l3 = []

for lista in (l1, l2):
    for elemento in lista:
        if elemento not in l3:  # Verifica se o elemento já existe em l3
            l3.append(elemento)
l3.sort()
print(l3)  