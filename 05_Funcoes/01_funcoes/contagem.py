def contador(i, f, p):
    if p == 0:
        print("O passo não pode ser 0! Considerando passo = 1.")
        p = 1
    if i > f and p > 0:
        p = -p
    for c in range(i, f + (1 if p > 0 else -1), p):
        print(f"{c}", end=' ')
    print("FIM")

contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input("inicio: "))
fim = int(input("fim: "))
passo = int(input("passo: "))
contador(inicio, fim, passo)
