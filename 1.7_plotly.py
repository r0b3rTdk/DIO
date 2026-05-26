'''
1. Importe a biblioteca plotly.express com o apelido px.
'''
import plotly.express as px
import pandas as pd

'''
2. Assim como o Seaborn, o Plotly tem datasets embutidos. Carregue o famoso dataset socioeconômico 
"Gapminder" usando dados = px.data.gapminder().
'''
dados = px.data.gapminder()

'''
3. Filtre os dados apenas para o ano de 2007 (você pode usar o método .query("year == 2007") nativo do pandas).
'''
ano_2007 = dados.query("year == 2007")

'''
4. Crie um gráfico de dispersão iterativo (px.scatter) com os dados filtrados. 
Coloque o PIB per capita (gdpPercap) no eixo X e a expectativa de vida (lifeExp) no eixo Y.
5. Adicione interatividade usando parâmetros adicionais dentro do px.scatter: 
passe a coluna continent para definir a cor (color), a coluna pop para definir o tamanho das bolhas (size) 
e a coluna country para o nome que aparece ao passar o mouse (hover_name).
'''
fig = px.scatter(
    ano_2007,
    x="gdpPercap",
    y="lifeExp",
    color="continent",
    size="pop",
    hover_name="country"
)

'''
6. Atribua o gráfico a uma variável (ex: fig = px.scatter(...)) e exiba-o utilizando o método .show() dessa variável.
'''
fig.show()