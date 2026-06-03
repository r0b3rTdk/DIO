n = int(input("digite o numero: "))
contador = 1
soma = 0
while n != 999:
    contador += 1
    soma += n
    n = int(input("digite o numero: "))
print(f"vc digitou {contador-1} antes de encerrar")
print(f"e o resultado da soma foi: {soma}")