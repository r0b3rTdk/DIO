numeros = (
    int(input("Digite o primeiro número: ")),
    int(input("Digite o segundo número: ")),
    int(input("Digite o terceiro número: ")),
    int(input("Digite o quarto número: "))
)

cont = 0

print(numeros)

print(f"O número 9 aparece {numeros.count(9)} vezes.")

if 3 in numeros:
    print(f"O primeiro índice do número 3 é: {numeros.index(3)+1}")
else:
    print("O número 3 não está presente na tupla.")

for i in numeros:
    if i % 2 == 0:
        cont += 1        
print(f"A quantidade de números pares é: {cont}")