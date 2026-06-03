valores = [[], [], []]


while True:
    valores[0].append(int(input("digite um numero: ")))
    
    resposta = input("vc quer adicionar novos numeros? [S/N] ").strip().upper()[0]
    while resposta not in 'SN':
        resposta = input("digite Sim ou Nao: ").strip().upper()[0]
    if resposta == 'N':
        break
    
for v in valores[0]:
    if v % 2 == 0:
        valores[1].append(v)
    else:
        valores[2].append(v)

valores[1].sort()
valores[2].sort()

print(f"o valores digitados foram: {valores[0]}")
print(f"o valores pares digitados foram: {valores[1]}")
print(f"o valores impares digitados foram: {valores[2]}")