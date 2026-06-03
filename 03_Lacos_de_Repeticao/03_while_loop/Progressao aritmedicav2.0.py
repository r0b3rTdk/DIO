primeiro_termo = int(input("digite o primeiro termo: "))
razao = int(input("digite de razao: "))


contador = 1
total = 0
mais = 10

while mais != 0:
    print(f"Os {mais} primeiros termos da PA são:")
    total += mais
    while contador <= total:
        print(primeiro_termo, end=' -> ')
        primeiro_termo += razao
        contador += 1
    mais = int(input("\nvoce quer mais quantos termos? "))

print(f"\no total de termos mostrados foi de {total}")