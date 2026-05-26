'''
1. Importe a biblioteca matplotlib.pyplot com o apelido padrão plt.
'''
import matplotlib.pyplot as plt

'''
2. Crie duas listas fictícias simples: dias = e usuarios_cadastrados = .
'''
dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
usuarios_cadastrados = [15, 30, 12, 40, 25]

'''
3. Crie um gráfico de linhas (plot) ou de barras (bar) cruzando essas duas listas (dias no eixo X, usuários no eixo Y).
'''
plt.bar(dias, usuarios_cadastrados)

'''
4. Adicione um título ao gráfico.
'''
plt.title("Novos Usuários Cadastrados por Dia")

'''
5. Adicione rótulos (labels) para o eixo X e para o eixo Y.
'''
plt.xlabel("Dias da Semana")
plt.ylabel("Quantidade de Usuarios")

'''
6. Exiba o gráfico na tela usando a função apropriada.
'''
plt.show()