from datetime import datetime

pessoa = {}
pessoa['nome'] = input("digite seu nome: ").strip().title()
ano = int(input("digite seu ano de nascimento: "))
ano_atual = datetime.now().year
pessoa['idade'] = ano_atual - ano
pessoa['ctps'] = int(input("dgigite o numero da carteira de trabalho: "))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input("digite o ano da contratacao: "))
    pessoa['salario'] = float(input("digite seu salario: "))
    pessoa['aposentadoria'] =  pessoa['idade'] + ((35 + pessoa['contratacao']) - ano_atual)

for k, v in pessoa.items():
    print(f"{k} = {v}")
    