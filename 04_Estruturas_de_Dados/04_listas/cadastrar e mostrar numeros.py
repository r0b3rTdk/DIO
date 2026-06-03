contador = 0
numero = []

while True:
    numero.append(int(input("digite um numero: ")))
    contador += 1
    
    resposta = input("voce quer continuar adicionando numeros? [S/N] ").strip().upper()[0]
    while resposta not in 'SN':
        resposta = input("Tente Novamente... voce quer continuar adicionando numeros? [S/N] ").strip().upper()[0]
        
    if resposta == 'N':
        break

print(f"foram digitados {contador} numeros")
numero.sort(reverse=True)
print(f"a lista e composta por: {numero}")

if 5 in numero:
    indice = numero.index(5)
    print(f"o 5 esta na lista na posicao {indice}")
else:
    print("o numero 5 nao esta na lista")
        
