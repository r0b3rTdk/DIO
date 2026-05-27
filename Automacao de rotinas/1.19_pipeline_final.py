'''
1. Importe load_breast_cancer de sklearn.datasets, train_test_split de sklearn.model_selection, 
LogisticRegression de sklearn.linear_model e accuracy_score de sklearn.metrics. 
Importe também sqlite3, seaborn como sns e matplotlib.pyplot como plt.
'''
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt

'''
2. Carregue os dados usando a função: X, y = load_breast_cancer(return_X_y=True).
'''
X, y = load_breast_cancer(return_X_y=True)

'''
3. Crie um gráfico de contagem (countplot do Seaborn) da variável alvo y para visualizarmos a proporção 
entre casos benignos e malignos. Exiba-o com plt.show().
'''
sns.countplot(x=y)
plt.title("Proporção entre casos Malignos (0) e Benignos (1)")
plt.xlabel("Diagnostico")
plt.ylabel("Quantidade")
plt.show()

'''
4. Divida os dados em treino (80%) e teste (20%) usando o random_state=42.
'''
X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)

'''
5. Instancie e treine o LogisticRegression apenas com os dados de treino 
(Dica: passe o parâmetro max_iter=10000 dentro dos parênteses do modelo para evitar avisos de limite de iterações).
'''
modelo = LogisticRegression(max_iter=10000)
modelo.fit(X_train, y_train)

'''
6. Faça a previsão nos dados de teste e calcule a métrica de acurácia.
'''
y_predict = modelo.predict(X_test)
accuracy = accuracy_score(y_test, y_predict)

'''
7. Conecte-se a um banco de dados SQLite chamado banco_metricas.db e garanta a criação de uma 
tabela chamada resultados (IF NOT EXISTS) com as colunas modelo (TEXT) e acuracia (REAL).
'''
conectar = sqlite3.connect("banco_metricas.db")
cursor = conectar.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS resultados(
        modelo TEXT,
        acuracia REAL           
    )
""")

'''
8. Insira uma nova linha no banco de dados contendo o nome do modelo (ex: "Regressão Logística") e o 
valor da acurácia calculada no passo 6, utilizando obrigatoriamente a boa prática dos placeholders ?.
'''
cursor.execute('INSERT INTO resultados (modelo, acuracia) VALUES(?, ?)', ("Regressão Logística", accuracy))

'''
9. Faça o commit, feche a conexão e imprima a acurácia final no terminal com um texto claro para o usuário.
'''
conectar.commit()
conectar.close()
print(f"Valor do accuracy com base nos testes: {accuracy * 100:.2f}%")