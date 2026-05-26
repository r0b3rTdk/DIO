'''
1.Crie uma função chamada processar_carrinho que receba uma lista de tuplas. Cada tupla representará um item e conterá 
uma string (nome do produto) e um float (preço). Exemplo: [("Camiseta", 50.0), ("Calça", 120.0), ("Meia", 15.0)].
'''
def processar_carrinho(produtos):
    '''
    2. Dentro da função, usando compreensão de lista (list comprehension), crie uma lista apenas com os nomes dos 
    produtos que custam 50.0 ou mais.
    '''
    produtos_caros = [nome for nome, preco in produtos if preco >= 50.0]

    '''
    3. Calcule o valor total de todos os itens do carrinho.
    '''
    valor_total = sum([preco for nome, preco in produtos])

    '''
    4. Se o valor total for maior que 150.0, aplique um desconto de 10% sobre o total.
    '''
    if valor_total > 150.0:
        valor_total = valor_total * 0.90

    total_pagar = valor_total
    '''
    5. A função deve retornar um dicionário contendo duas chaves: "produtos_caros" (recebendo a lista gerada no passo 2) 
    e "total_pagar" (recebendo o valor total final).
    '''
    dicionario = {"produtos_caros" : produtos_caros, "total_pagar" : total_pagar}
    return dicionario

'''
6. Fora da função, crie uma lista de tuplas com pelo menos 3 itens, chame a função e imprima o dicionário retornado.
'''
lista_produtos = [
    ("Camiseta", 50.0), ("Calça", 120.0), ("Meia", 15.0)
]

print(processar_carrinho(lista_produtos))