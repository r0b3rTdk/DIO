'''
1. Abra (ou crie) um arquivo chamado registro_acessos.txt em modo de adição (append).
'''
with open("registro_acessos.txt", "a") as arquivo:
    '''
    2. Escreva duas novas mensagens simulando logs de acesso (por exemplo: "Acesso de Joao", "Acesso de Maria"), 
    garantindo a quebra de linha.
    '''
    arquivo.write("Acesso de r0b3rT\n")
    arquivo.write("Acesso de Brands\n")

'''
3. Em seguida, abra o arquivo em modo de leitura.
'''
with open("registro_acessos.txt", "r") as arquivo:
    '''
    4. Usando um loop for diretamente no objeto do arquivo, leia e exiba linha por linha no terminal, 
    mas adicione o prefixo [LIDO]:  antes de imprimir o conteúdo de cada linha.
    '''
    for linhas in arquivo:
        print(f"[LIDO]: {linhas.strip()}")


    