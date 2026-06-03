preco = float(input("Digite o preco da mercadoria: "))
perc_desconto = int(input("Digite o percentual de desconto: "))
desconto = preco * (perc_desconto / 100)
valor_pagar = preco - desconto  
print(f"O desconto ficou de R${desconto}, o valor total a pagar e de: R${valor_pagar}")
