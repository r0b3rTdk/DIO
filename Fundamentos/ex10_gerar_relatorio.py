'''
1. Crie uma função chamada gerar_relatorio que receba uma lista de dicionários. Cada dicionário representa um candidato 
e possui as seguintes chaves: "nome" (string), "idade" (int) e "habilidades" (lista de strings). 
Exemplo de entrada: [{"nome": "Ana", "idade": 25, "habilidades": ["Python", "SQL"]}, 
{"nome": "João", "idade": 30, "habilidades": ["Java", "Python"]}].
'''
def gerar_relatorio(candidatos):
    '''
    2. Dentro da função, calcule a média de idade de todos os candidatos.
    '''
    media = sum([candidato['idade'] for candidato in candidatos]) / len(candidatos)

    '''
    3. Crie um conjunto (set) contendo todas as habilidades únicas de todos os candidatos 
    (juntando as habilidades de todos em um único conjunto para remover repetições).
    '''
    habilidades_unicas = set()
    for candidato in candidatos:
        habilidades_unicas.update(candidato['habilidades'])
    
    '''
    4. A função deve retornar um dicionário final contendo duas chaves exatas: "media_idades" (com o valor da média) 
    e "habilidades_unicas" (com o conjunto de habilidades).
    '''
    dicionario = {"media_idades" : media, "habilidades_unicas" : habilidades_unicas}
    return dicionario
'''
5. Fora da função, crie uma lista contendo dados de pelo menos 3 candidatos, chame a função passando essa lista e 
imprima o dicionário retornado.
'''
dados_candidatos = [
    {
        "nome": "r0b3rT", 
        "idade": 26, 
        "habilidades": ["Python", "SQL"]
    },
    {
        "nome": "Renan", 
        "idade": 20, 
        "habilidades": ["Python", "Java"]
    },
    {
        "nome": "Teto", 
        "idade": 30, 
        "habilidades": ["Java", "SQL"]
    }
]

print(gerar_relatorio(dados_candidatos))