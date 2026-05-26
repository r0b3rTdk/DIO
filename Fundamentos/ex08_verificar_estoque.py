'''
1. Crie uma função chamada verificar_estoque que receba um dicionário onde a chave é o nome de um produto (string) 
e o valor é a sua quantidade em estoque (int).
'''
def verifificar_estoque(estoque):
    '''
    2. Dentro da função, crie uma lista vazia chamada disponiveis e um conjunto vazio chamado faltantes 
    (lembre-se da sintaxe para criar um set vazio, pois {} cria um dicionário).
    '''
    disponiveis = []
    faltantes = set()
    '''
    3. Itere sobre os itens do dicionário (tanto a chave quanto o valor ao mesmo tempo).
    '''
    for nomes, quantidade_estoque in estoque.items():
        '''
        4. Se a quantidade for maior que zero, adicione o nome do produto na lista disponiveis, convertido para maiúsculas.
        '''
        
        if quantidade_estoque > 0:
            disponiveis.append(nomes.upper())
        else:
            faltantes.add(nomes.lower())
        '''
        5. Se a quantidade for zero, adicione o nome do produto ao conjunto faltantes, convertido para minúsculas.
        '''
        '''
        6. A função deve retornar uma tupla contendo a lista de disponíveis (na primeira posição) e o conjunto de faltantes 
        (na segunda posição).
        '''
    return disponiveis, faltantes

'''
7. Fora da função, crie o dicionário: produtos = {"Teclado": 10, "Mouse": 0, "Monitor": 5, "Webcam": 0}.
'''
estoque = {
    "Teclado" : 10,
    "Mouse" : 0,
    "Monitor" : 5,
    "Webcam" : 0
}

'''
8. Chame a função passando esse dicionário e imprima o resultado.
'''
print(verifificar_estoque(estoque))