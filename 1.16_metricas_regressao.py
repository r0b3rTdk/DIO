'''
1. Importe train_test_split e make_regression exatamente como no exercício anterior.
'''
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression

'''
2. Importe o modelo LinearRegression de sklearn.linear_model.
'''
from sklearn.linear_model import LinearRegression

'''
3. Importe as métricas mean_absolute_error, root_mean_squared_error e r2_score de sklearn.metrics.
'''
from sklearn.metrics import r2_score, root_mean_squared_error, mean_absolute_error

'''
4. Gere o dataset (com make_regression) e faça a divisão de 80% treino e 20% teste (com train_test_split),
da mesma forma que antes.
'''
X, y = make_regression(n_samples=100, n_features=5, noise=20.0, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

'''
5. Instancie e treine o modelo LinearRegression apenas com os dados de treino.
'''
modelo = LinearRegression()
modelo.fit(X_train, y_train)

'''
6. Faça as previsões do modelo para os dados de teste usando o método .predict() e guarde o resultado 
(ex: y_pred = modelo.predict(X_test)).
'''
y_predict = modelo.predict(X_test)

'''
7. Calcule e exiba no terminal as três métricas avaliando o modelo nos dados de teste (comparando o y_test com o y_pred).
'''
r2 = r2_score(y_test, y_predict)
print(f"R² (Score): {r2:.2f}")

rmse = root_mean_squared_error(y_test, y_predict)
print(f"Raiz do Erro Quadrático Médio (RMSE): {rmse:.2f}")

mae = mean_absolute_error(y_test, y_predict)
print(f"Erro Absoluto Médio (MAE): {mae:.2f}")