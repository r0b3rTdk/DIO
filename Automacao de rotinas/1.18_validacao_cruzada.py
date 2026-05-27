'''
1. Importe cross_val_score de sklearn.model_selection, o modelo LogisticRegression de sklearn.linear_model 
e make_classification de sklearn.datasets.
'''
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

'''
2. Gere o dataset com X, y = make_classification(n_samples=300, n_features=5, random_state=42).
'''
X, y = make_classification(n_samples=300, n_features=5, random_state=42)

'''
3. Instancie o modelo modelo = LogisticRegression(). (Atenção: não faça o .fit(), 
a validação cruzada fará isso automaticamente por debaixo dos panos).
'''
modelo = LogisticRegression()

'''
4. Utilize a função passando o modelo, o X, o y, e definindo 5 divisões com o parâmetro cv=5 
(ex: scores = cross_val_score(modelo, X, y, cv=5)). Opcionalmente, você pode explicitar scoring='accuracy'.
'''
scores = cross_val_score(modelo, X, y, cv=5, scoring='accuracy')

'''
5. Imprima a lista de resultados gerada (você verá 5 notas diferentes).
'''
print(f"Scores: {scores}")

'''
6. Imprima também a média dessas notas (scores.mean()) e o desvio padrão (scores.std()) 
para avaliar o quão estável o modelo é ao longo das diferentes divisões.
'''
print(f"Media: {scores.mean()}")
print(f"Desvio Padrao: {scores.std()}")