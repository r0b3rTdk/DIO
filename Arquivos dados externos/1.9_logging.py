'''
1. Importe o módulo embutido logging.
'''
import logging
'''
2. Configure o sistema de logs usando logging.basicConfig(). Defina o arquivo de saída (argumento filename) 
como app.log, o modo de abertura (argumento filemode) como "w" (para sobrescrever a cada execução) e o 
nível mínimo (argumento level) para logging.INFO.
'''
logging.basicConfig(filename="app.log", filemode="w", level=logging.INFO)
'''
3. Gere três mensagens de log distintas usando os próprios métodos do módulo:
Uma mensagem de nível debug (ex: "Checando variáveis internas").
Uma mensagem de nível info (ex: "Processamento iniciado").
Uma mensagem de nível error (ex: "Falha ao processar o arquivo").
'''
logging.debug("Checando variáveis internas")
logging.info("Processamento iniciado")
logging.error("Falha ao processar o arquivo")
'''
1. Em seguida, usando o with, abra o arquivo app.log em modo de leitura e imprima seu conteúdo no terminal. 
(Se você configurou certo, a mensagem de debug não deve aparecer no arquivo lido).
'''
with open("app.log", "r") as arquivo:
    print(arquivo.read())