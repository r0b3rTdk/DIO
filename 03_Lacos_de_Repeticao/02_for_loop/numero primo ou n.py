num = int(input("\033[mdigite um numero: "))
total = 0
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[33m', end = " ")
        total += 1
    else:
        print('\033[31m', end = " ")
    print(f"{c}", end= " ")
print(f"\n\033[mO numero {num} foi divisivel {total} vezes")
if total == 2:
    print(f"o numero {num} e PRIMO")
else:
    print(f"o numero {num} NAO e primo")