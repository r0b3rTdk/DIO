salario = float(input("qual o seu salario? "))
porc_aumento = int(input("qual a porcentagem de aumento? "))
aumento = salario * (porc_aumento / 100)
aumento_total = aumento + salario
print(f"o aumento sera {aumento}, no total sera: {aumento_total}")