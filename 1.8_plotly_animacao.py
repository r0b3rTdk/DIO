'''
1. Carregue o dataset inteiro usando dados = px.data.gapminder().
'''
import plotly.express as px

dados = px.data.gapminder()

'''
2. Crie o mesmo gráfico de dispersão (px.scatter) 
cruzando gdpPercap (X) e lifeExp (Y), com continent na cor, pop no tamanho e country no hover_name.
3. Adicione o parâmetro animation_frame="year" para criar um botão de "play" que fará a animação país por país 
ao longo das décadas.
4. Adicione o parâmetro facet_col="continent" para dividir o gráfico em painéis lado a lado, um para cada continente.
5. Como a animação muda os valores a cada ano, o gráfico pode ficar pulando. 
Para estabilizar, adicione os seguintes parâmetros de ajuste: log_x=True, size_max=45, range_x=e range_y= .
'''
fig = px.scatter(
    dados,
    x="gdpPercap",
    y="lifeExp",
    color="continent",
    size="pop",
    hover_name="country",
    animation_frame="year",
    facet_col="continent",
    log_x=True,
    size_max=45,
    range_x=[100, 100000],
    range_y=[25, 90]
)

'''
6. Exiba o gráfico na tela.
'''
fig.show()