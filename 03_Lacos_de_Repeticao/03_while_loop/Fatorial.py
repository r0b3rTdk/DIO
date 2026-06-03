num = int(input("digite o numero: "))
resultado = 1
contador = num
print(f"\ncalculando {num}!...\n")
while contador > 0:
#for i in range(1, contador + 1):
    print(f"{contador}", end='')
    if contador > 1:
        print(" x ", end= '')
    else:
        print(" = ", end= '')
    resultado = contador * resultado
    contador -= 1
    
print(f"{resultado}")

