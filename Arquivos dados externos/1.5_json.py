'''
1. Importe o módulo embutido json.
'''
import json
'''
2. Crie um dicionário Python contendo dados de um cliente (exemplo: {"nome": "Alice", "idade": 30, "ativo": True}).
'''
dados = {
    "nome": "r0b3rT", 
    "idade": 26,
    "ativo": True
}

'''
3. Abra um arquivo chamado cliente.json em modo de escrita (w) usando o with.
'''
with open("cliente.json", "w") as arquivo:
    '''
    4. Use a função json.dump() para salvar esse dicionário dentro do arquivo.
    '''
    json.dump(dados, arquivo)

'''
5. Em seguida, abra o mesmo arquivo em modo de leitura (r).
'''
with open("cliente.json", "r") as arquivo:
    '''
    6. Use a função json.load() para carregar os dados de volta para uma nova variável.
    '''
    dados = json.load(arquivo)

'''
7. Imprima no terminal apenas o nome do cliente acessando a chave "nome" desse novo dicionário lido.
'''
print(dados["nome"])
