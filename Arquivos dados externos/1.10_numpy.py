'''
1. Importe a biblioteca numpy usando o apelido padrão que a comunidade utiliza (dica: são duas letras).
'''
import numpy as np
'''
2. Crie um array NumPy a partir de uma lista simples contendo os seguintes valores de vendas diárias: 120, 150, 200, 130.
'''
vendas_dia = np.array([120, 150, 200, 130])
'''
3. Faça uma operação vetorizada para aplicar um aumento de 10% a todos os elementos do array de uma vez só 
(dica: multiplique por 1.1) e guarde em uma nova variável.
'''
resultado = vendas_dia * 1.1
'''
4. Calcule e imprima a média das vendas atualizadas usando o método estatístico apropriado do NumPy.
'''
print(resultado.mean())