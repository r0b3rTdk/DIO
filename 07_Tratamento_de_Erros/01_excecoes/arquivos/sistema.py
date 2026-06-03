from interface import *
from pessoascadastradas import *

arq = 'pessoascadastradas.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

cabecalho('MENU PRINCIPAL')
while True:
    resposta = menu(['listar pessoas', 'cadastrar pessoas', 'sair do sistema'])
    if resposta == 1:
        # opcao para listar pessoas do arquivo
        lerArquivo(arq)
    
    elif resposta == 2:
        cabecalho("NOVO CADASTRO")
        nome = input("nome: ")
        idade = leiaInt("idade: ")
        cadastrar(arq, nome, idade)
    
    elif resposta == 3:
        cabecalho("saindo do sistema... ate mais")
        break
    
    else:
        print("\033[0;031mvoce nao digitou uma opcao valida\033[m")

