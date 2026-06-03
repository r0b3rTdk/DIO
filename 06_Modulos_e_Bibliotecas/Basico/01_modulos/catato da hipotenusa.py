import math
cateto_oposto = float(input("digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("digite o comprimento do cateto adjacente: "))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print(f"o resultado da hipotenusa e: {hipotenusa:.3}")