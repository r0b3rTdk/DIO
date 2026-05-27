'''
1. Importe seaborn como sns e matplotlib.pyplot como plt.
'''
import seaborn as sns
import matplotlib.pyplot as plt

'''
2. Carregue o dataset sobre gorjetas usando dados = sns.load_dataset("tips").
'''
dados = sns.load_dataset("tips")

'''
3. Crie um gráfico de contagem (countplot) para visualizar a frequência de cada categoria nos dias da semana 
(coluna day). Exiba com plt.show().
'''
sns.countplot(data=dados, x="day")
plt.show()

'''
4. Crie um histograma (histplot) para analisar como os valores totais das contas estão distribuídos 
(coluna total_bill). Exiba com plt.show().
'''
sns.histplot(dados["total_bill"])
plt.show()

'''
5. Crie um gráfico de dispersão (scatterplot) cruzando o valor da conta (total_bill no eixo X) e a 
gorjeta (tip no eixo Y) para ver como essas variáveis numéricas se relacionam. Exiba com plt.show().
'''
sns.scatterplot(data=dados, x="total_bill", y="tip")
plt.show()

'''
6. Crie um boxplot para comparar a distribuição dos valores das contas
(total_bill no eixo Y) agrupadas por dia da semana (day no eixo X). Exiba com plt.show().
'''
sns.boxplot(data=dados, x="day", y="total_bill")
plt.show()