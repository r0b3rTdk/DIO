"""
1. Crie uma função chamada analisar_texto que receba uma string contendo uma frase.
"""
def analisar_texto(frase):
    """
    2. Dentro da função, divida a frase em uma lista de palavras 
    (lembre-se de qual método de string faz isso).
    """
    lista_palavras = frase.split()
    """
    3. Transforme essa lista em um conjunto (set) para descobrir a quantidade de palavras únicas 
    (já que conjuntos não aceitam itens repetidos).
    """
    quantidade_palavras = set(lista_palavras)

    """
    4. A função deve retornar um dicionário com duas chaves: "total_palavras" 
    (a quantidade total de itens na lista) e "palavras_unicas" (a quantidade de itens no conjunto).
    """
    dicionario = {
        "total_palavras" : len(lista_palavras),
        "palavras_unicas" : len(quantidade_palavras)
    }
    return dicionario

"""
5. Fora da função, crie uma variável com o texto: "aprender python é aprender a pensar em python".
"""
texto = "aprender python é aprender a pensar em python"

"""
6. Chame a função passando o texto e imprima o dicionário retornado.
"""
print(analisar_texto(texto))