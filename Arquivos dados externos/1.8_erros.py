'''
3. Envolva toda essa lógica em uma estrutura try/except.
'''
try:
    '''
    1. Tente abrir um arquivo chamado config.txt em modo de leitura (r) usando o with.
    '''
    with open("config.txt", "r") as arquivo:
        '''
        2. Dentro do bloco do with, leia o conteúdo do arquivo, converta o valor lido para um número inteiro e 
        divida o número 100 por esse valor. Imprima o resultado da divisão.
        '''
        conteudo = int(arquivo.read())
        resultado = 100 / conteudo
        print(resultado)
    '''
    4. Capture especificamente três tipos de exceção em blocos except separados
    (regra obrigatória: não use except: genérico):
        FileNotFoundError (imprima uma mensagem de arquivo não encontrado).
        ValueError (imprima uma mensagem avisando que o conteúdo não é um número válido).
        ZeroDivisionError (imprima uma mensagem de erro de divisão por zero).
    '''
except ZeroDivisionError:
    print("erro de divisão por zero")
except ValueError:
    print("o conteúdo não é um número válido")
except FileNotFoundError:
    print("arquivo não encontrado)")
    '''
    5. Adicione um bloco finally ao final de tudo que imprima: "Processo de leitura finalizado."
    '''
finally:
    print("processo de leitura finalizado.")

