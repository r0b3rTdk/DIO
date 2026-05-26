'''
1. Importe train_test_split de sklearn.model_selection e a função make_classification de sklearn.datasets.
'''
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

'''
2. Importe o modelo LogisticRegression de sklearn.linear_model.
'''
from sklearn.linear_model import LogisticRegression

'''
3. Importe as métricas accuracy_score, precision_score, recall_score e f1_score de sklearn.metrics.
'''
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

'''
4. Gere o dataset binário usando: X, y = make_classification(n_samples=200, n_features=4, random_state=42).
'''
X, y = make_classification(n_samples=200, n_features=4, random_state=42)

'''
5. Faça a divisão dos dados na proporção 80% treino e 20% teste (lembre-se do random_state=42).
'''
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

'''
6. Instancie e treine o modelo LogisticRegression apenas com os dados de treino.
'''
modelo = LogisticRegression()
modelo.fit(X_train, y_train)

'''
7. Faça as previsões do modelo para os dados de teste (ex: y_pred = modelo.predict(X_test)).
'''
y_predict = modelo.predict(X_test)

'''
8. Calcule e exiba no terminal as quatro métricas (Acurácia, Precisão, Recall e F1) 
avaliando o modelo nos dados de teste.
'''
accuracy = accuracy_score(y_test, y_predict)
print(f"Proporção total com base em ACCURACY: {accuracy}")

precision = precision_score(y_test, y_predict)
print(f"Proporção total com base em PRECISION: {precision}")

recall = recall_score(y_test, y_predict)
print(f"Proporção total com base em RECALL: {recall}")

f1 = f1_score(y_test, y_predict)
print(f"Proporção total com base em F1: {f1}")