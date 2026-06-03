pessoas = []
mulher = []
maior = []
pessoa = {'nome': '', 'sexo': '', 'idade': 0}
soma = 0

while True:
    pessoa['nome'] = input("digite seu nome: ")
    pessoa['sexo'] = input("digite o sexo [M/F]: ").strip().upper()[0]
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = input("tente novamente... digite o sexo [M/F]: ").strip().upper()[0]
    pessoa['idade'] = int(input("qual sua idade? "))
    soma += pessoa['idade']
    if pessoa['sexo'] == 'F':
        mulher.append(pessoa.copy())
    if pessoa['idade'] >= 18:
        maior.append(pessoa.copy())
    pessoas.append(pessoa.copy())
    r = input("quer adicionar mais pessoas? [S/N] ").strip().upper()[0]
    while r not in 'SN':
        r = input("tente novamente... quer adicionar mais pessoas? [S/N] ").strip().upper()[0]
    if r == 'N':
        break

total = len(pessoas)
media = soma / total 

print("-"*30)
print(f"foram cadastradas {total} pessoas")
print(f"a media de idade foi: {media:.2f}")
if len(mulher) != 0:
    print("\nLista de mulheres cadastradas:")
    for m in mulher:
        print(f"Nome: {m['nome']}, Idade: {m['idade']}")
if len(maior) != 0:
    print("\nLista de maior de idade cadastrados:")
    for m in maior:
        print(f"Nome: {m['nome']}, Idade: {m['idade']}")
