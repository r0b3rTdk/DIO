print("-=-" * 20)
print("analizador de triangulos")
print("-=-" * 20)

r1 = float(input("Digite a medida da reta 1: "))
r2 = float(input("Digite a medida da reta 2: "))
r3 = float(input("Digite a medida da reta 3: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Pode ser um triângulo.")
else:
    print("Não pode ser um triângulo.")