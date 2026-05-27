'''
1. Importe matplotlib.pyplot como plt e seaborn como sns.
'''
import matplotlib.pyplot as plt
import seaborn as sns

'''
2. Carregue o dataset de gorjetas usando dados = sns.load_dataset("tips").
'''
dados = sns.load_dataset("tips")

'''
3. Crie uma figura e uma grade de eixos com 1 linha e 2 colunas usando o comando fig, ax = plt.subplots(1, 2).
'''
fig, ax = plt.subplots(1, 2)

'''
4. No primeiro painel, crie um histograma (histplot) do Seaborn para a variável total_bill. 
Para garantir que ele fique no lado esquerdo, passe o parâmetro ax=ax dentro da chamada do Seaborn.
'''
sns.histplot(dados["total_bill"], ax=ax[0])

'''
5. No segundo painel, crie um gráfico de dispersão (scatterplot) 
cruzando total_bill (eixo X) e tip (eixo Y). Direcione-o para o lado direito passando o parâmetro ax=ax.
'''
sns.scatterplot(data=dados, x="total_bill", y="tip", ax=ax[1])

'''
6. Utilize a função plt.tight_layout() logo após os gráficos. Essa é uma excelente boa prática para ajustar 
os espaçamentos e evitar que textos e eixos fiquem sobrepostos.
'''
plt.tight_layout()

'''
7. Exiba a figura completa na tela com plt.show().
'''
plt.show()
