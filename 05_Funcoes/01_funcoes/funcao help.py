cores = ('\033[m',         # sem cor
         '\033[0;30;41m',  # vermelho
         '\033[0;30;42m',  # verde
         '\033[0;30;43m',  # amarelo
         '\033[0;30;44m',  # azul
         '\033[0;30;45m',  # roxo
         '\033[7;30m'      # branco
         );

def ajuda(com):
    titulo(f"acessando o manual do comando \'{com}\'", 4)
    print(cores[6], end='')
    help(com)
    print(cores[0], end='')

def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tamanho)
    print(f"  {msg}")
    print('~' * tamanho)
    print(cores[0], end='')


comando = ''
titulo("PROJETO HELPPY", 2)
while True:
    comando = input("funcao ou biblioteca: ").lower().strip()
    if comando == 'fim':
        titulo("FIM DO PROGRAMA HELPPY", 1)
        break
    else:
        ajuda(comando)