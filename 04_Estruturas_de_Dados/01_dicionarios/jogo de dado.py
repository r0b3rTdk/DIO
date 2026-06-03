import random
from time import sleep
from operator import itemgetter
jogo = {
    'jogador1' : random.randint(1, 6),
    'jogador2' : random.randint(1, 6),
    'jogador3' : random.randint(1, 6),
    'jogador4' : random.randint(1, 6)}
ranking = {}
print("Valores sorteados:")
for k, v in jogo.items():
    print(f"{k} tirou {v} no dado")
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate(ranking):
    print(f"{i+1} lugar: {v[0]} com {v[1]}")