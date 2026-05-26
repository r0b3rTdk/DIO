'''
1. Importe o pandas, o numpy e o matplotlib.pyplot usando seus apelidos padrões.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
2. Simule dados vindos de um sistema externo criando um DataFrame a partir deste dicionário: 
{"Vendedor": ["Lucas", "Mariana", "Lucas", "Mariana", "Carlos"], "Vendas": [150.0, np.nan, 200.0, 300.0, np.nan]}
'''
dados = {
    "Vendedor": ["Lucas", "Mariana", "Lucas", "Mariana", "Carlos"], 
    "Vendas": [150.0, np.nan, 200.0, 300.0, np.nan]
}

df = pd.DataFrame(dados)

'''
3. Faça a limpeza dos dados: preencha todos os valores nulos (np.nan) da coluna "Vendas" com o valor numérico 0 (zero).
'''
df["Vendas"] = df["Vendas"].fillna(0)

'''
4. Usando o método de agrupamento do Pandas, calcule a soma total de vendas agrupada por cada "Vendedor".
'''
calculo = df.groupby("Vendedor").sum()

'''
5. Salve o resultado desse agrupamento em um arquivo chamado relatorio_vendas.csv 
(pode deixar o índice ser exportado desta vez, pois o agrupamento transforma o nome do vendedor no índice).
'''
calculo.to_csv("relatorio_vendas.csv")

'''
6. Usando os dados agrupados, crie um gráfico de barras mostrando o vendedor no eixo X e o total vendido no eixo Y.
'''
plt.bar(calculo.index, calculo["Vendas"])

'''
7. Adicione título ao gráfico e rótulos (labels) para os dois eixos, e exiba o gráfico na tela.
'''
plt.title("Vendas dos vendedores")
plt.xlabel("Vendedor")
plt.ylabel("Vendas")
plt.show()