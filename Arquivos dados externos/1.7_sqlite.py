'''
1. Importe o módulo embutido sqlite3.
'''
import sqlite3

'''
2. Abra uma conexão com um banco de dados chamado meubanco.db usando sqlite3.connect().
'''
conexao = sqlite3.connect("meubanco.db")

'''
3. Crie um objeto cursor a partir da conexão.
'''
cursor = conexao.cursor()

'''
4. Use o cursor para executar (execute) uma instrução SQL que crie uma tabela chamada usuarios com duas colunas: 
id (INTEGER PRIMARY KEY) e nome (TEXT). 
Dica: você pode usar IF NOT EXISTS na criação da tabela para evitar erros ao rodar o script mais de uma vez.
'''
cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
               id INTEGER PRIMARY KEY,
               nome TEXT
        )
""")

'''
5. Insira um novo usuário na tabela (por exemplo, "Roberto"). Requisito obrigatório: 
Você deve usar o placeholder ? para passar o valor do nome. Nunca use f-strings para injetar valores no SQLite.
'''
# Note que adicionamos (nome) para indicar a coluna, VALUES no plural 
# e a vírgula depois de "Roberto" para formar a tupla corretamente.
cursor.execute(
    "INSERT INTO usuarios (nome) VALUES (?)",
    ("Robert",)
)

'''
6. Confirme a transação salvando as alterações com commit().
'''
conexao.commit()

'''
7. Faça uma consulta (SELECT) para buscar todos os registros da tabela usuarios.
'''
cursor.execute("SELECT * FROM usuarios")

'''
8. Extraia os dados com fetchall() e imprima o resultado no terminal.
'''
dados = cursor.fetchall()
print(dados)

'''
9. Requisito obrigatório: Feche a conexão com o banco de dados no final.
'''
conexao.close()