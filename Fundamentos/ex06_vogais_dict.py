"""
1. Crie uma função chamada contar_vogais que receba uma string como parâmetro.
"""
def contar_vogais(vogais):
    """
    2. A função deve iterar pela string e contar a ocorrência de cada vogal ('a', 'e', 'i', 'o', 'u'), 
    ignorando a diferença entre letras maiúsculas e minúsculas.
    """
    dicionario = {
        "a" : 0,
        "e" : 0,
        "i" : 0,
        "o" : 0,
        "u" : 0
    }
    """
    3. Armazene e retorne o resultado em um dicionário, onde a chave é a vogal e o valor é a 
    quantidade de vezes que ela apareceu no texto.
    """
    for vogal in vogais:
        if vogal.lower() in "aeiou":
            dicionario[vogal.lower()] += 1
    
    return dicionario

"""
4. Fora da função, crie uma variável com o texto: 
"O pensamento computacional resolve problemas complexos".
"""
texto = "O pensamento computacional resolve problemas complexos"

"""
5. Chame a função passando esse texto e imprima o dicionário retornado.
"""

print(contar_vogais(texto))
