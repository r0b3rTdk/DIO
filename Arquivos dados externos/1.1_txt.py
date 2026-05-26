'''
1. Abra um arquivo chamado log_simples.txt em modo de escrita.
'''
with open("log_simples.txt", "w") as arquivo:
    '''
    2. Escreva três linhas diferentes nele (por exemplo, três nomes de frutas, uma em cada linha).
    '''
    arquivo.write("isso e serio\n")
    arquivo.write("xtranho\n")
    arquivo.write("japones")
    
'''
3. Em seguida, abra o mesmo arquivo em modo de leitura e exiba o seu conteúdo completo na tela.
'''
with open("log_simples.txt", "r") as arquivo:
    conteudo = arquivo.read()

print(conteudo)





