'''
1. Importe o módulo embutido csv.
'''
import csv
'''
2. Abra um arquivo chamado produtos.csv em modo de escrita. Requisito: use o argumento newline="" no open() 
para evitar linhas em branco extras ao salvar o arquivo.
'''
with open("produtos.csv", "w", newline="") as arquivo:
    '''
    3. Usando o csv.writer, escreva uma linha de cabeçalho contendo ["Produto", "Preco"].
    '''
    writer = csv.writer(arquivo)

    writer.writerow(["Produto", "Preco"])

    '''
    4. Em seguida, escreva duas linhas de dados (exemplo: ["Teclado", 150] e ["Mouse", 80]).
    '''
    writer.writerow(["Teclado", 150])
    writer.writerow(["Mouse", 80])

'''
4. Por fim, abra o mesmo arquivo em modo de leitura, passe o arquivo para o csv.reader 
e use um loop for para imprimir cada linha do arquivo no terminal.
'''
with open("produtos.csv", "r") as arquivo:
    reader = csv.reader(arquivo)

    for linha in reader:
        print(linha)


