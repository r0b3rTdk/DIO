'''
1. Importe seaborn como sns e matplotlib.pyplot como plt.
'''
import seaborn as sns
import matplotlib.pyplot as plt

'''
2. Carregue o dataset de gorjetas usando dados = sns.load_dataset("tips").
'''
dados = sns.load_dataset("tips")

'''
3. Crie uma figura com 2 linhas e 2 colunas usando fig, ax = plt.subplots(2, 2).
'''
fig, ax = plt.subplots(2, 2)

'''
4. No painel superior esquerdo (ax), crie o gráfico ideal para responder: 
"Qual a frequência total de clientes atendidos por dia da semana (day)?"
'''
sns.countplot(data=dados, x="day", ax=ax[0, 0])

'''
5. No painel superior direito (ax), crie o gráfico ideal para responder: 
"Como estão distribuídos os valores gerais de todas as gorjetas dadas (tip)?"
'''
sns.histplot(dados["tip"], ax=ax[0, 1])

'''
6. No painel inferior esquerdo (ax), crie o gráfico ideal para responder: 
"Como podemos comparar a distribuição das gorjetas (tip) separando por fumantes e não fumantes (smoker)?"
'''
sns.boxplot(data=dados, x="tip", y="smoker", ax=ax[1, 0])

'''
7. No painel inferior direito (ax), crie o gráfico ideal para responder: 
"Qual a relação entre o tamanho da mesa (size) e o valor total da conta (total_bill)?"
'''
sns.scatterplot(data=dados, x="size", y="total_bill", ax=ax[1, 1])

'''
8. Utilize plt.tight_layout() logo após os gráficos e, em seguida, exiba a figura com plt.show().
'''
plt.tight_layout()
plt.show()