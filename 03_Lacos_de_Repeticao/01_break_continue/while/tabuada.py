numero = int(input("digite um numero: [digite um numero negativo pra parar] "))
contador = 1

while True:
    if numero < 0:
        break
    print(f"\n\ntabuada de {numero}")
    print(f"-=-"*20)
    
    for i in range(1, 11):
        resultado = i * numero
        
        print(f"{numero} x {i} = {resultado}")
    print(f"-=-"*20)

    contador += 1
    numero = int(input("\ndigite um numero: [digite 0 pra parar] "))
    
print(f"voce obteve {contador} resultados de tabuadas")
