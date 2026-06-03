valor_produto = float(int("digite o valor base do produto: "))
print("-=-"*20)
print("1 - dinheiro/pix")
print("2 - a vista cartao")
print("3 - em ate 2x no cartao")
print("4 - 3x ou mais no cartao")
escolha = int(input("qual a opcao de pagamento? "))

if escolha == 1:
    valor_final = valor_produto - (valor_produto * 0.10)
    print(f"o valor final e de {valor_final}")
elif escolha == 2:
    valor_final = valor_produto - (valor_produto * 0.05)
    print(f"o valor final e de {valor_final}")
elif escolha == 3:
    print(f"o valor final e de {valor_produto}")
elif escolha == 4:
    valor_final = valor_produto + (valor_produto * 0.20)
    print(f"o valor final e de {valor_final}")
else: 
    print("opcao inavalida")
