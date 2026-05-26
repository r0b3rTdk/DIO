'''
1. Importe o pandas e o numpy usando os apelidos padrões.
'''
import pandas as pd
import numpy as np
'''
2. Crie um DataFrame a partir do seguinte dicionário de passageiros, que contém dados ausentes (np.nan): 
{"Nome": ["Ana", "Bruno", "Carlos", "Daniela"], "Idade": [25, np.nan, 30, np.nan], "Tarifa": [50.0, 80.0, 30.0, 100.0]}
'''
dados = {
    "Nome": ["Ana", "Bruno", "Carlos", "Daniela"], 
    "Idade": [25, np.nan, 30, np.nan], 
    "Tarifa": [50.0, 80.0, 30.0, 100.0]
}

df = pd.DataFrame(dados)

'''
3. Usando a combinação de dois métodos do Pandas, calcule e imprima no terminal a soma de valores nulos em cada coluna.
'''
print(df.isnull().sum())

'''
4. Em seguida, preencha os valores nulos da coluna "Idade" com a média das idades válidas dessa mesma coluna.
'''
df["Idade"] = df["Idade"].fillna(df["Idade"].mean())

'''
5. Imprima o DataFrame atualizado no terminal para confirmar que os valores nulos foram substituídos corretamente.
'''
print(df)