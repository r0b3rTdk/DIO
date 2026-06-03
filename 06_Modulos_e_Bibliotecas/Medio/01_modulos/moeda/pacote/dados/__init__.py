# pacote/dados.py
def leiaMoeda(msg):
    while True:
        entrada = input(msg).strip().replace(',', '.')
        try:
            num = float(entrada)
            return num
        except ValueError:
            print("\033[0;31mErro! Por favor, digite um valor válido.\033[m")
