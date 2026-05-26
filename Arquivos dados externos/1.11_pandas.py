'''
1. Importe a biblioteca pandas usando o apelido padrão da comunidade.
'''
import pandas as pd

'''
2. Crie um dicionário Python contendo três chaves: "Produto", "Preco" e "Quantidade". 
Preencha cada chave com uma lista de três valores correspondentes à sua escolha.
'''
dados = {
    "Produto": ["Placa de video", "Monitor", "Gabinete"],
    "Preco": [700, 600, 250],
    "Quantidade": [4, 3, 2]
}

'''
3. Converta esse dicionário em um Pandas DataFrame.
'''
df = pd.DataFrame(dados)

'''
4. Salve esse DataFrame em um arquivo chamado estoque.csv. Requisito obrigatório: 
passe o argumento necessário para não exportar a coluna de índice do DataFrame para o arquivo.
'''
df.to_csv("estoque.csv", index=False)

'''
5. Em seguida, leia o arquivo estoque.csv que você acabou de criar de volta para uma nova variável.
'''
df = pd.read_csv("estoque.csv")

'''
6. Imprima esse novo DataFrame no terminal e, logo abaixo, imprima também um resumo estatístico das colunas numéricas 
(dica: existe um método específico do Pandas que calcula média, mínimo, máximo, etc., de uma só vez).
'''
print(df)
print(df.describe())