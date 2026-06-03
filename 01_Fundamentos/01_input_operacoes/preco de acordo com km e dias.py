km_percorridos = float(input("Digite a quantidade de quilômetros percorridos: "))
dias_alugados = int(input("Digite a quantidade de dias de aluguel: "))

preco_por_km = 0.15
preco_por_dia = 60

custo_km = km_percorridos * preco_por_km
custo_dias = dias_alugados * preco_por_dia
preco_total = custo_km + custo_dias

print(f"O total a pagar é de R${preco_total}")