'''
1. Importe a função train_test_split de sklearn.model_selection.
'''
from sklearn.model_selection import train_test_split

'''
2. Crie dados fictícios simples onde o X (as características) é uma lista de listas e o y (o alvo) é uma lista simples. 
Exemplo: X = [3,4,5,6,7,8,9,10] e y = [4].
'''
x = [
    [1, 2], [3, 4], [5, 6], [7, 8], [9, 10], 
    [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]
]
y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

'''
3. Use a função train_test_split para dividir essas listas em 4 variáveis: X_train, X_test, y_train, y_test.
4. Garanta a proporção de 80% para treino e 20% para teste passando o 
parâmetro test_size=0.2 e garanta a reprodutibilidade passando random_state=42.
'''
X_train, X_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,
    random_state=42
)

'''
5. Exiba no terminal o tamanho (len()) de X_train e X_test para comprovar que ficaram com 8 e 2 itens, respectivamente.
'''
print(f"Tamanho do X_train: {len(X_train)}")
print(f"Tamanho do X_test: {len(X_test)}")