from interface import *

def arquivoExiste(nome):
    try:   #vai abrir e fechar o arquivo se ele existir
        a = open(nome, 'rt') #rt significa ler o arquivo
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #wt+ signifia q vai criar um arquivo de texto
        a.close()
    except:
        print("houve um ERRO na criacao do arquivo")
    
        
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        cabecalho("ERRO ao ler o arquivo")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        for linha in a:
            dado = linha.split(';') #vai dividir os dados
            dado[1] = dado[1].replace('\n', '')
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close()

def cadastrar(arq, nome = '<desconhecido>', idade = 0):
    try:
        a = open(arq, 'at') #vai escrever dentro do arquivo
    except:
        print("\033[0;031mhouve um ERRO na abertura do arquivo\033[m")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("\033[0;031mhouve um ERRO na hora de ler os arquivos\033[m")
        else:
            print(f"novo registro de {nome} adicionado")
            a.close()
