n = int(input("qual o numero escolhido? "))
mult = 0
for c in range (1, 11):
    mult += 1
    print(f"{n} x {mult} = {n * mult}")
print("FIM")