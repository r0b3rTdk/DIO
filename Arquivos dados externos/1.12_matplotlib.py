'''
1. Importe o pandas e o módulo matplotlib.pyplot usando os apelidos padrões da comunidade.
'''
import pandas as pd
import matplotlib.pyplot as plt

'''
2. Recrie o DataFrame com os mesmos dados do exercício anterior (Produto, Preço e Quantidade).
'''
dados = {
    "Produto": ["Placa de video", "Monitor", "Gabinete"],
    "Preco": [700, 600, 250],
    "Quantidade": [4, 3, 2]
}

df = pd.DataFrame(dados)

'''
3. Usando a interface do pyplot, crie um gráfico de barras onde o eixo X representa os nomes dos produtos 
e o eixo Y representa os preços.
'''
plt.bar(df["Produto"], df["Preco"])

'''
4. Adicione um título ao gráfico e rótulos (labels) para os eixos X e Y.
'''
plt.title("Preco dos produtos")
plt.xlabel("Produtos")
plt.ylabel("Preço (R$)")

'''
5. Exiba o gráfico na tela usando o método correto de exibição do Matplotlib.
'''
plt.show()