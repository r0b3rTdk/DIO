valores = []
for v in range(1, 6):
    numero = int(input(f"digite o {v} valor: "))
    
    if v == 1 or numero > valores[-1]:
        valores.append(numero)
    else:
        pos = 0
        while pos < len(valores):
            if numero <= valores[pos]:
                valores.insert(pos, numero)
                break
            pos += 1    
    
print(f"os numeros cadastrados foram: {valores}")