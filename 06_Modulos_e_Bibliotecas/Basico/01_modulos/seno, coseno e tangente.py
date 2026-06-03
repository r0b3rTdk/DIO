import math
angulo = float(input("digite o angulo: "))
seno = math.sin(math.radians(angulo))
print(f"o angulo de {angulo} tem o seno de {seno:.2}")
cosseno = math.cos(math.radians(angulo))
print(f"o angulo de {angulo} tem o cosseno de {cosseno}")
tangente = math.tan(math.radians(angulo))
print(f"o angulo de {angulo} tem a tangente de {tangente}")