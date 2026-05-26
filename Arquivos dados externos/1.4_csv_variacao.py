import csv
'''
1. Abra o arquivo produtos.csv (que você acabou de criar) em modo de adição (a), 
lembrando do requisito obrigatório de usar o with e newline="".
'''
with open("produtos.csv", "a", newline="") as arquivo:
    writer = csv.writer(arquivo)
    '''
    2. Adicione apenas mais um produto usando o csv.writer (exemplo: ["Monitor", 600]).
    '''
    writer.writerow(["Monitor", 600])

'''
3. Em seguida, abra o mesmo arquivo em modo de leitura.
'''
with open("produtos.csv", "r") as arquivo:
    '''
    4. Usando o csv.reader, itere pelo arquivo e imprima no terminal apenas o nome do produto 
    (ou seja, o primeiro item de cada linha da lista), ignorando os preços.
    '''
    reader = csv.reader(arquivo)

    for linha in reader:
        print(linha[0])


