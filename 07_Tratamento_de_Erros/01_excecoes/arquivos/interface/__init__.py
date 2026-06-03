def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except:
            print("\033[0;031mvoce nao digitou uma opcao valida\033[m")

def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    c = 1
    for item in lista:
        print(f"\t\033[33m{c}\033[m - \t\033[34m{item}\033[m")
        c += 1
    print(linha())
    opc = leiaInt("\033[34msua opcao: \033[m")
    return opc
    