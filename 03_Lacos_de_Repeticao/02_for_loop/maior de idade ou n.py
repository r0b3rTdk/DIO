from datetime import date
anoatual = date.today().year
maior_idade = 0
menor_idade = 0
for i in range (1, 8):
    ano = int(input("digite seu ano de nascimento: "))
    idade = anoatual - ano
    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1
print(f"{maior_idade} pessoas sao maiores de idade e {menor_idade} sao menores")