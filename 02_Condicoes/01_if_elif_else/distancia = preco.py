distancia = float(input("digite a distancia que vc deseja percorrer: "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
    
print(f"o preco sera de R${preco}")