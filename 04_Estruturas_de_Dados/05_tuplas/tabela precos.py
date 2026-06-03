listagem = (
    'coca', 9.0,
    'mouse', 120,
    'teclado', 200,
    'monitor', 900,
    'camisa de time', 300,
    'short cargo', 80,
    'casaco', 130,
    'perfume', 180,
    'oculos', 30
)

print(f"-"*35)
print(f"{'LISTA DE PREÇOS':^35}")
print(f"-"*35)

for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(f"{listagem[i]:.<30}", end= '')
    else:
        print(f"R${listagem[i]:>.2f}")
print(f"-"*35)
