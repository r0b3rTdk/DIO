dados = []
pessoas = []
contador = 0

while True:
    nome = input("Digite seu nome: ").strip().upper()
    peso = int(input("Digite seu peso: "))
    dados.append(nome)
    dados.append(peso)
    
    pessoas.append(dados[:])
    dados.clear()  # Limpa `dados` para a próxima entrada
    contador += 1
   
    r = input("quer adicionar mais alguma pessoa? [S/N] ").strip().upper()[0]
    while r not in 'SN':
        r = input("digite sim ou nao... quer adicionar mais alguma pessoa? [S/N] ").strip().upper()[0]
    if r == 'N':
        break
# Calcula maior e menor peso
maior_peso = max(p[1] for p in pessoas)
menor_peso = min(p[1] for p in pessoas)

# Filtra as pessoas com o maior e menor peso
mais_pesadas = [p[0] for p in pessoas if p[1] == maior_peso]
mais_leves = [p[0] for p in pessoas if p[1] == menor_peso]

print(f"Foram adicionadas {contador} pessoas.")
print(f"As pessoas mais pesadas são {mais_pesadas} com {maior_peso} kg.")
print(f"As pessoas mais leves são {mais_leves} com {menor_peso} kg.")

"""
p[1] for p in pessoas: Isso é uma expressão que pega o peso de cada pessoa na lista pessoas. O [1] refere-se ao segundo elemento de cada sublista (que é o peso).

Exemplo: Se pessoas = [['JOÃO', 70], ['MARIA', 65]], a expressão p[1] for p in pessoas vai criar uma lista [70, 65], que são os pesos de João e Maria.
max(p[1] for p in pessoas): Essa parte encontra o maior número na lista de pesos.
min(p[1] for p in pessoas): Essa parte encontra o menor número na lista de pesos.

[p[0] for p in pessoas if p[1] == maior_peso]: Isso é uma "compreensão de lista", que cria uma nova lista contendo apenas as pessoas com o maior peso.
p[0]: Aqui estamos pegando o nome ([0] é o primeiro item, que é o nome) de cada pessoa p em pessoas.

if p[1] == maior_peso: Verificamos se o peso da pessoa (p[1]) é igual ao maior_peso. Se for, o nome dela (p[0]) é adicionado à nova lista mais_pesadas.
[p[0] for p in pessoas if p[1] == menor_peso]: Da mesma forma, isso cria uma lista mais_leves contendo apenas as pessoas que têm o menor peso.

Exemplo para Clarificar
Imagine que pessoas seja:


pessoas = [['JOÃO', 70], ['MARIA', 65], ['ANA', 70], ['PEDRO', 60]]
Calculando o Maior e o Menor Peso

maior_peso = max(p[1] for p in pessoas) → A lista de pesos é [70, 65, 70, 60], então maior_peso será 70.
menor_peso = min(p[1] for p in pessoas) → A lista de pesos é [70, 65, 70, 60], então menor_peso será 60.
Filtrando as Pessoas com o Maior Peso

mais_pesadas = [p[0] for p in pessoas if p[1] == maior_peso]:
Aqui, a condição if p[1] == maior_peso será verdadeira para ['JOÃO', 70] e ['ANA', 70].
Então mais_pesadas será ['JOÃO', 'ANA'].
Filtrando as Pessoas com o Menor Peso

mais_leves = [p[0] for p in pessoas if p[1] == menor_peso]:
Aqui, a condição if p[1] == menor_peso será verdadeira apenas para ['PEDRO', 60].
Então mais_leves será ['PEDRO'].
Após essa filtragem:

print(mais_pesadas)  # Saída: ['JOÃO', 'ANA']
print(mais_leves)    # Saída: ['PEDRO']
Resumo
Usamos max() e min() para encontrar os valores máximo e mínimo de uma lista de pesos.
Usamos uma "compreensão de lista" com uma condição if para filtrar as pessoas que têm esses pesos específicos.
"""