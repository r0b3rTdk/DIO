"""
1. Crie um dicionário contendo os dados de um aluno. Ele deve ter duas chaves iniciais: 
"nome" (contendo o nome do aluno em string) e "notas" (contendo uma lista com três notas numéricas, 
por exemplo, [7.5, 6.0, 9.0]).
"""
dados_aluno = {
    "nome": "Robert", 
    "notas": [7.5, 6.0, 9.0]
}

"""
2. Calcule a média das notas desse aluno acessando a lista dentro do dicionário 
(não use os números diretamente na conta, extraia do dicionário).
"""
#media = (dados_aluno["notas"][0] + dados_aluno["notas"][1] + dados_aluno["notas"][2]) / 3
media = sum(dados_aluno["notas"]) / len(dados_aluno["notas"])

"""
3. Adicione uma nova chave a esse dicionário chamada "status".
"""
#dados_aluno["status"]

"""
4. Usando uma estrutura condicional (if/else), atribua à chave "status" o valor "Aprovado" 
se a média for maior ou igual a 7.0. Caso contrário, atribua o valor "Reprovado".
"""
if media >= 7.0:
    dados_aluno["status"] = "Aprovado"
else:
    dados_aluno["status"] = "Reprovado"

"""
5. Imprima uma mensagem usando f-string que exiba o nome, a média 
(formatada para exibir exatamente 2 casas decimais) e o status do aluno.
"""
print(f"O Aluno {dados_aluno["nome"]} teve a media {media:.2f}, Status: {dados_aluno["status"]}")