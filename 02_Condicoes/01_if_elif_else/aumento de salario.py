salario = float(input("digite o seu salario: "))

if salario >= 1.250:
    aumento = salario * (10/100)
if salario < 1.250:
    aumento = salario * (15/100)
    
total = salario + aumento

print(f"o aumento sera de R${aumento}, e ficando no total com R${total}")