'''
1. Importe o módulo requests e o módulo json.
'''
import json
import requests
'''
2. Faça uma requisição do tipo GET para a API pública do ViaCEP usando a URL: https://viacep.com.br/ws/01001000/json/.
'''
url = "https://viacep.com.br/ws/01001000/json/"
resposta = requests.get(url)
'''
3. Verifique se o status_code da resposta é 200 (que indica sucesso).
'''
if resposta.status_code == 200:
    '''
    4. Se for sucesso, extraia os dados da resposta no formato dicionário usando o método .json() do objeto da resposta.
    '''
    dados = resposta.json()

    '''
    5. Usando o with, abra um arquivo chamado endereco.json em modo de escrita (w).
    '''
    with open("endereco.json", "w") as arquivo:
        '''
        6. Salve o dicionário extraído da API dentro desse arquivo usando json.dump().
        '''
        json.dump(dados, arquivo)
    print(dados)

else:
    print("Falha na requisição. Status:", resposta.status_code)