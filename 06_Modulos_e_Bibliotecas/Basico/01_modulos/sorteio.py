import random
aluno1 = input("primeiro aluno: ")
aluno2 = input("segundo aluno: ")
aluno3 = input("terceiro aluno: ")
aluno4 = input("quarto aluno: ")
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print(f"o aluno escolhido foi {escolhido}")