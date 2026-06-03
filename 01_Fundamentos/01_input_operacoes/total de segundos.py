dias = int(input("digite o numero de dias: "))
horas = int(input("digite o numero de horas: "))
minutos = int(input("digite o numero de minutos: "))
segundos = int(input("digite o numero de segundos: "))
total_segundos = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos
print(f"o total de segundos e: {total_segundos}")