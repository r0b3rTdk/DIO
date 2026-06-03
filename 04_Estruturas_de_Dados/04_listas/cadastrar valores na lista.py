valores = []
while True:
    numero = int(input("adicione um numero: "))
    if numero in valores:
        print("o valor ja foi adicionado")
    else:
        valores.append(numero)       
    resposta = input("quer continuar adicionando numeros? [S/N]  ").strip().upper()[0]
    
    while resposta not in 'SN':
        resposta = input("Tente Novamente... quer continuar adicionando numeros? [S/N]  ").strip().upper()[0]
    if resposta == 'N':
        break    

valores.sort()
print(f"Lista de valores únicos: {valores}")