valor_casa = float(input("digite o valor da casa: "))
salario = float(input("digite o valor do seu salario: "))
anos = float(input("digite a quantidade de anos para quitar: "))

prestacao = valor_casa / (anos * 12)
trinta = salario * 30/100

if prestacao > trinta:
    print("o valor da prestacao excedeu os 30%")
else:
    print(f"o valor foi aprovado, a prestacao ficara de {prestacao:.2f}")
