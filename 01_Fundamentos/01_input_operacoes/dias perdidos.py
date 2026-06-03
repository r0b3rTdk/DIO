cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
anos_fumando = int(input("Há quantos anos você fuma? "))

minutos_perdidos_por_cigarro = 10
minutos_perdidos_por_dia = cigarros_por_dia * minutos_perdidos_por_cigarro
minutos_perdidos_total = minutos_perdidos_por_dia * 365 * anos_fumando

dias_perdidos = minutos_perdidos_total // (24 * 60)

print(f"Você perdeu aproximadamente {dias_perdidos} dias de vida devido ao fumo.")
