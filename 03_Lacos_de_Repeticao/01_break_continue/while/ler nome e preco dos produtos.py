total_gasto = 0
quantos_produtos = 0
nome_barato = ''
menor = 0
contador = 0

while True:
    print("\nCADASTRAR PRODUTOS")
    print("-"*20)
    nome = input("digite o nome do produto: ")
    preco = int(input("digite o preco: R$"))

    contador += 1
    # Verifica se é o primeiro produto ou se o preço atual é menor que o menor preço encontrado
    if contador == 1:
        menor = preco
        nome_barato = nome
    else:
        if preco < menor:
            menor = preco
            nome_barato = nome
    
    total_gasto += preco
    if preco > 1000:
        quantos_produtos += 1  
    
    escolha = ' '
    while escolha not in 'SN':
        escolha = input("vc quer continuar? [S/N]  ").strip().upper()[0]
    if escolha == 'N':
        break

print(f"o total de gastos em todos os {contador} produtos foi de R${total_gasto:.2f}")
print(f"teve {quantos_produtos} produtos comprados acima do R$1.000,00")
print(f"o produto com o menor preco foi {nome_barato} com o valor de R${menor:.2f}")
