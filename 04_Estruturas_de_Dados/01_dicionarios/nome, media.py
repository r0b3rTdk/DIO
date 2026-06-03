aluno = {}
aprovado = []
final = []
reprovado = []

for i in range(0, 3):
    aluno.clear()
    aluno['nome'] = input("digite seu nome: ").strip().title()
    aluno['media'] = float(input(f"digite a media de {aluno['nome']}: "))

    if aluno['media'] >= 7:
        aprovado.append(aluno.copy())
    elif 5 <= aluno['media'] < 7:
        final.append(aluno.copy())
    else:
        reprovado.append(aluno.copy())

        
print("\nAlunos Aprovados:")
for i in aprovado:
    print(f"O aluno {i['nome']} foi aprovado com média {i['media']}")
print("\nAlunos na Final:")
for i in final:
    print(f"o aluno {i['nome']} esta na final com media {i['media']}")
print("\nAlunos Reprovados:")
for i in reprovado:
    print(f"O aluno {i['nome']} foi reprovado com média {i['media']}")