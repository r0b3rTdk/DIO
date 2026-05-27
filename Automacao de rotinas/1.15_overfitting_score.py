'''
1. Importe train_test_split de sklearn.model_selection, DecisionTreeRegressor de sklearn.tree e a 
função make_regression de sklearn.datasets 
(essa última serve para gerar um dataset falso mais complexo do que listas na mão).
'''
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.datasets import make_regression

'''
2. Gere os dados de características (X) e alvo (y) usando: X, 
y = make_regression(n_samples=100, n_features=5, noise=20.0, random_state=42).
'''
X, y = make_regression(n_samples=100, n_features=5, noise=20.0, random_state=42)

'''
3. Faça a divisão dos dados (80% treino, 20% teste) exatamente como você fez no exercício anterior.
'''
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

'''
4. Instancie o modelo usando modelo = DecisionTreeRegressor(random_state=42) e treine-o 
(usando o método .fit()) apenas com os dados de treino.
'''
modelo = DecisionTreeRegressor(random_state=42).fit(X_train, y_train)

'''
5. Avalie a qualidade do modelo extraindo o R² (usando o método .score()) nos dados de treino. Guarde em uma variável.
'''
qualidade_modelo_treino = modelo.score(X_train, y_train)

'''
6. Faça a mesma avaliação de R² (usando .score()), mas agora passando os dados de teste. Guarde em outra variável.
'''
qualidade_modelo_teste = modelo.score(X_test, y_test)

'''
7. Exiba os dois resultados no terminal usando print().
'''
print(f"Qualidade do modelo nos dados de TREINO: {qualidade_modelo_treino:.2f}")
print(f"Qualidade do modelo nos dados de TESTE: {qualidade_modelo_teste:.2f}")