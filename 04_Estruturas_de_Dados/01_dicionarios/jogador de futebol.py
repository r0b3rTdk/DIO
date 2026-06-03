jogadores = []
gols = []

while True:
    print("=-="*30)
    jogador = {'nome': '', 'gols': [], 'partidas': 0, 'total': 0, 'media': 0}

    nome = input("digite o nome do jogador: ").title().strip()
    jogador['nome'] = nome
    quant_part = int(input(f"quantas partidas {jogador['nome']} fez: "))
    jogador['partidas'] = quant_part
    total = 0

    for i in range(quant_part):
        gol = int(input(f"quantos gols {jogador['nome']} fez na partida {i + 1}: "))
        total += gol   
        gols.append(gol)
    jogador['gols'] = gols
    jogador['total'] = total
    jogador['media'] = total / quant_part if quant_part > 0 else 0
    jogadores.append(jogador.copy())
    
    r = input("vc quer adicionar mais jogadores? [S/N] ").strip().upper()[0]
    while r not in 'SN':
        r = input("tente novamente... vc quer adicionar mais jogadores? [S/N] ").strip().upper()[0]
    if r == 'N':
        break


print(f"\n{'Cod.':<4} {'Nome':<8} {'gols':>15} {'total':>10}")
print(f"{'-'*30}")

for i, jogador in enumerate(jogadores):
    print(f"{i:<4} {jogador['nome']:<8} {str(jogador['gols']):>15} {jogador['total']:>10}")

while True:
    print(f"{'-'*30}")
    opc = int(input("quer ver os detalhes de qual jogador? [999 pra sair] "))
    if opc == 999:
        break
    if opc <= len(jogadores) - 1:
        print(f"\n-- DETALHES DO JOGADOR {jogadores[opc]['nome']} --")
        for i, k in enumerate(jogadores[opc]['gols']):
            print(f"Na partida {i+1}, ele fez {k} gols")
        print(f"Total de gols: {jogadores[opc]['total']}")
        print(f"Média de gols por partida: {jogadores[opc]['media']:.2f}")
