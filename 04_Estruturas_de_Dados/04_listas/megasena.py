import random

print(f"{'-'*30}")
print(f"{'Mega Sena':^30}")
print(f"{'-'*30}")

jogos = int(input("quantos jogos vc que gerar? "))

todos_jogos = []

for i in range(jogos):
    jogo = []
    while len(jogo) < 6:
        numero = random.randint(1, 60)
        if numero not in jogo:
                jogo.append(numero)
    todos_jogos.append(jogo)

for i, jogo in enumerate(todos_jogos):
    jogo.sort()
    print(f"Jogo {i+1}: {jogo}")

'''
start=1 faz a contagem começar em 1, para que 
o primeiro jogo seja Jogo 1, o segundo seja Jogo 2, e assim por diante.
'''