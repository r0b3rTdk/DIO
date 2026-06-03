brasileirao = ('Botafogo','Palmeiras','Flamengo','Sao Paulo','Fortaleza','Inter','Vasco','Bahia','Cruzeiro','Atletico-MG','Gremio','Vitoria','Fluminense','Criciuma','Corinthians','Bragantino','Atletico-PR','Juventude','Cuiaba','Atletico-GO')

print(f"os cinco primeiros colocados sao: {brasileirao[0:5]}")
print(f"o Z4 atualmente esta composto por: {brasileirao[16:]}")
print(sorted(brasileirao))
print(f"o SOBERANO esta na posicao: {brasileirao.index('Sao Paulo')+1}")