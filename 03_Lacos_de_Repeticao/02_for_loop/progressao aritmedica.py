primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

print("Os 10 primeiros termos da PA são:")

for i in range(1, 11):
  print(primeiro_termo, end= " ")
  primeiro_termo += razao
 
print("FIM")