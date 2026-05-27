'''
1. Faça uma requisição GET simples para uma URL qualquer (por exemplo, https://api.github.com) 
utilizando a biblioteca nativa ou requests.
'''
import requests, datetime, logging

logging.basicConfig(level=logging.INFO)

url = "https://api.github.com"

'''
2. Capture o código de status (status_code) da resposta.
'''
resposta = requests.get(url)

codigo_status = resposta.status_code

'''
3. Utilize a biblioteca datetime para capturar a data e hora exatas do momento da requisição.
'''
hora_exata = datetime.datetime.now()

'''
4. Exiba no terminal uma mensagem contendo o horário da execução e o status code retornado.
'''
""
logging.info(f"requisicao feita em {hora_exata} com status_code {codigo_status}")