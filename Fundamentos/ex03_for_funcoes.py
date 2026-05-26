"""
1. Crie uma função chamada filtrar_alunos que deve receber um único parâmetro: 
uma lista contendo vários dicionários de alunos (com a mesma estrutura do exercício anterior, 
tendo "nome" e "status").
"""
def filtrar_alunos(lista_alunos):
    """
    2. Dentro da função, crie duas listas vazias: aprovados e reprovados.
    """
    aprovados = []
    reprovados = []

    """
    3. Use um laço de repetição (for) para iterar (percorrer) a lista de alunos recebida.
    """
    for aluno in lista_alunos:
        """
        4. A cada volta do laço, verifique o valor da chave "status" do aluno atual. 
        Se for "Aprovado", adicione o "nome" dele na lista aprovados. Caso contrário, 
        adicione na lista reprovados.
        """
        if aluno['status'] == 'Aprovado':
            aprovados.append(aluno['nome'])
        else:
            reprovados.append(aluno['nome'])
    """
    5. Faça a função retornar as duas listas (aprovados e reprovados) ao mesmo tempo. 
    Diferente de outras linguagens, em Python uma função pode retornar múltiplos valores.
    """
    return aprovados, reprovados

"""
6. Fora da função, crie uma lista chamada turma contendo pelo menos 3 dicionários de alunos. 
Você pode inventar os dados, garantindo que tenham pelo menos as chaves "nome" e "status".
"""
turma = [
    {
        "nome": "Robert",
        "status": "Aprovado"
    },
     {
        "nome": "Renan",
        "status": "Aprovado"
    },
    {
        "nome": "Renato",
        "status": "Reprovado"
    }
]

"""
7. Chame a sua função filtrar_alunos passando a lista turma como argumento, guarde os dois valores 
retornados em variáveis e imprima os nomes dos alunos aprovados e reprovados.
"""

lista_aprovados, lista_reprovados = filtrar_alunos(turma)

print("Aprovados: ")
for aluno in lista_aprovados:
    print(aluno)

print("\nReprovados: ")
for aluno in lista_reprovados:
    print(aluno)