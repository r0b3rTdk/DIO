"""
1. Crie uma variável contendo uma tupla chamada temperaturas com os seguintes valores numéricos 
flutuantes: 22.5, 30.0, 15.5, 28.0, 19.0, 26.5. Lembre-se da sintaxe para criar tuplas.
"""
temperaturas = (22.5, 30.0, 15.5, 28.0, 19.0, 26.5)

"""
2. Tentar alterar um valor dentro de uma tupla (como temperaturas = 25.0) daria erro, 
pois elas são imutáveis. Sendo assim, use uma Compreensão de Lista (List Comprehension) 
para gerar uma nova estrutura: crie uma lista chamada temperaturas_altas que filtre a 
tupla e guarde apenas as temperaturas maiores que 25.0.
"""
temperaturas_altas = [temperatura for temperatura in temperaturas if temperatura > 25.0]

"""
3. Imprima uma frase formatada mostrando a quantidade total de temperaturas registradas 
(da tupla original) e, em seguida, imprima a lista temperaturas_altas. 
Dica: Você pode usar a função embutida len() para contar a quantidade de itens.
"""
print(f"Quantidade total de temperaturas registradas: {len(temperaturas)}")
print(f"Lista de temperaturas acima de 25.0: {temperaturas_altas}")