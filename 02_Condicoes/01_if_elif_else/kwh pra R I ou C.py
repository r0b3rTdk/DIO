kwh = float(input("digite o kWh consumido: "))
print("R - Residencias")
print("I - Industrias")
print("C - Comercios")

# Definindo as variáveis R, I e C como strings
R = 'R'
I = 'I'
C = 'C'

instalacao = input("digite o tipo de instalacao: ")

if instalacao == R:
    if kwh > 500:
        preco = kwh * 0.65
        print("o valor a pagar sera de R$%.2f" % preco)
    else:
        preco = kwh * 0.40
        print("o valor a pagar sera de R$%.2f" % preco)
elif instalacao == I:
    if kwh > 5000:
        preco = kwh * 0.60
        print("o valor a pagar sera de R$%.2f" % preco)
    else:
        preco = kwh * 0.55
        print("o valor a pagar sera de R$%.2f" % preco)
elif instalacao == C:
    if kwh > 1000:
        preco = kwh * 0.60
        print("o valor a pagar sera de R$%.2f" % preco)
    else:
        preco = kwh * 0.55
        print("o valor a pagar sera de R$%.2f" % preco)
else:
    print("Erro: Tipo de instalação inválido. Por favor, digite R, I ou C.")