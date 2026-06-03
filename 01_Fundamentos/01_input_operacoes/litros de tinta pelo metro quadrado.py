altura = float(input("digite a altura: "))
largura = float(input("digite a largura: "))

area = altura * largura
tinta = area / 2

print(f"sua parede tem a dimensao de {altura}x{largura} e sua area e de {area:.3f}m2")
print(f"voce vai precisar de {tinta:.5f} para pintar sua parede")