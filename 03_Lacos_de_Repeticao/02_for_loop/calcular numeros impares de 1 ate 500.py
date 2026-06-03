soma = 0 #acumulador = soma + algo
cont = 0 #contador = contador + 1
for c in range (1, 501 , 2):
  if c % 3 == 0:
    cont += 1
    soma += c
print(f"todos os {cont} somados tem o valor de {soma}")