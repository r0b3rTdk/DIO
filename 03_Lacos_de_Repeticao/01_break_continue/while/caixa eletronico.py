print("="*30)
print(f"{' BANCO ':=^30}")
print("="*30)

valor = float(input("digite o valor a ser sacado: "))
total = valor
ced = 100
totalced = 0

while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f"{totalced} cédulas de R${ced}")
        totalced = 0  # Reseta o contador de cédulas após exibir o resultado para a cédula atual
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        if total == 0:
            break
        
print("="*30)
print(f"SAQUE REALIZADO! VOLTE SEMPRE")
print("="*30)
