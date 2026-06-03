def ficha(jogador, gols):
    if jogador == "":  # Se o nome estiver vazio, usa o padrão
        jogador = "<desconhecido>"
    if gols == "":
        gols = 0
    print(f"o jogador {jogador} fez {gols} gols")

j = input("digite o nome do jogador: ").strip()
g = input("quantos gols ele fez? ").strip()
ficha(j, g)
    