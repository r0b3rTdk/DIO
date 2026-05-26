"""
1. Crie dois conjuntos (sets) contendo os IDs numéricos de alunos matriculados em dois cursos 
diferentes. Crie o curso_python = {101, 102, 103, 104} e o curso_sql = {103, 104, 105, 106}. 
Lembre-se que sets usam chaves {} assim como os dicionários, mas não possuem o formato "chave: valor"
"""
curso_python = {101, 102, 103, 104}
curso_sql = {103, 104, 105, 106}

"""
2. Usando uma operação ou método de conjuntos, descubra quais IDs estão matriculados em ambos 
os cursos ao mesmo tempo (ou seja, a interseção entre eles) e guarde em uma variável chamada 
alunos_ambos.
"""
alunos_ambos = curso_python & curso_sql

"""
3. Usando o método adequado, adicione o ID 107 ao conjunto curso_python.
"""
curso_python.add(107)

"""
4. Crie um dicionário vazio chamado relatorio. Adicione uma chave "dupla_matricula" a ele, 
contendo como valor o conjunto alunos_ambos gerado no passo 2.
"""
relatorio = {
    "dupla_matricula" : alunos_ambos
}

"""
5. Imprima o dicionário relatorio.
"""
print(relatorio)