soma = 0
for i in range (1, 7):
    n = int(input(f"digite o {i} numero: "))
    if n % 2 == 0:
        soma += n
print(f"a soma de todos os numeros pares deu: {soma}")
print("FIM")