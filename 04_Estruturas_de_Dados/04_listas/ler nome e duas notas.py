
print(f"{'-'*30}")
print(f"{'CENTRAL DE NOTAS':^30}")
print(f"{'-'*30}")

sala = []

while True:
    
    nome = input("digite o seu nome: ").strip()
    nota_1 = float(input("digite sua primeira nota: "))
    nota_2 = float(input("digite sua segunda nota: "))
    
    media = (nota_1 + nota_2) / 2
    
    sala.append([nome, nota_1, nota_2, media])

    r = input("quer adicionar mais alunos? [S/N] ").strip().upper()[0]
    while r not in 'SN':
        r = input("tente novamente... quer adicionar mais alunos? [S/N] ").strip().upper()[0]
    if r == 'N':
        break

print(f"{'-'*30}")
print(f"{'BOLETIM DE NOTAS':^30}")
print(f"{'-'*30}")

print(f"\n{'Cod.':<4} {'Nome':<8} {'Média':>8}")
print(f"{'-'*30}")

for i, aluno in enumerate(sala):
    print(f"{i:<4} {aluno[0]:<8} {aluno[3]:>8.1f}")

while True:
    print(f"{'-'*30}")
    opc = int(input("quer ver as notas de qual aluno, digite o codigo: [999 pra sair] "))
    if opc == 999:
        break
    if opc <= len(sala) - 1:
        print(f"Notas de {sala[opc][0]} são {sala[opc][1]:.1f} e {sala[opc][2]:.1f}")
'''
for i in range(jogos):
    jogo = []
    while len(jogo) < 6:
        numero = random.randint(1, 60)
        if numero not in jogo:
                jogo.append(numero)
    todos_jogos.append(jogo)

for i, jogo in enumerate(todos_jogos, start=1):
    print(f"Jogo {i}: {jogo}")


start=1 faz a contagem começar em 1, para que 
o primeiro jogo seja Jogo 1, o segundo seja Jogo 2, e assim por diante.
'''