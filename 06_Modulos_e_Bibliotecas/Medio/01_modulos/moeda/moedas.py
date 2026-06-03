from pacote import dados, moeda

preco = dados.leiaMoeda("digite o preco: R$")
resp = input("digite 0 pra diminuir ou 1 para aumentar o valor: ").strip().upper()[0]
while resp not in '01':
    resp = input("digite 0 pra diminuir ou 1 para aumentar o valor: ").strip().upper()[0]
if resp == '1':
    taxa = int(input("digite a porcentagem do aumento: "))
else: 
    taxa = int(input("digite a porcentagem da diminuicao: "))

moeda.resumo(preco, taxa, resp)