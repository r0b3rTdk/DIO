'''
1. Faça uma requisição GET para https://jsonplaceholder.typicode.com/users/1.
'''
import logging, requests, datetime, json

logging.basicConfig(level=logging.INFO)

url = "https://jsonplaceholder.typicode.com/users/1"

'''
2. Utilize o comando assert para verificar se o status_code é 200 antes de prosseguir com o script.
'''
resposta = requests.get(url)

assert (resposta.status_code) == 200

'''
3. Extraia o conteúdo da resposta no formato JSON (a biblioteca requests tem um método nativo para isso).
'''
dados = resposta.json()

'''
4. Salve esses dados em um arquivo local chamado dados_usuario.json, utilizando a 
biblioteca nativa json e garantindo o uso do with open(...). 
'''
with open("dados_usuario.json", "w") as arquivo:
    json.dump(dados, arquivo)
    '''
    5. Adicione um logging.info que registre o horário exato em que o arquivo foi salvo com sucesso.
    '''
    hora_exata = datetime.datetime.now()
    logging.info(f"Arquivo salvo com sucesso em: {hora_exata}")