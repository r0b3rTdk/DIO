'''
1. Importe a biblioteca sqlite3 e crie uma conexão com um banco local chamado banco_usuarios.db.
'''
import sqlite3, logging, datetime

logging.basicConfig(level=logging.INFO)

conexao = sqlite3.connect("banco_usuarios.db")
cursor = conexao.cursor()
'''
2. Crie uma tabela chamada usuarios com as colunas id (INTEGER) e nome (TEXT).
Lembre-se de usar a instrução correta para evitar que o script quebre na segunda execução caso a tabela já exista.
'''
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT,
        nome TEXT
    ) 
""")
tabela_criada = datetime.datetime.now()

'''
3. Insira um usuário fictício (ex: id 1, nome 'Alice') no banco de dados. 
Atenção à boa prática obrigatória: use ? como placeholder para passar os valores no execute, prevenindo injeção de SQL.
'''
cursor.execute("INSERT INTO usuarios (id, nome) VALUES(?, ?)", (1, "Alice"))
insercao_finalizada = datetime.datetime.now()

'''
4. Confirme a transação para gravar os dados (commit).
'''
conexao.commit()
'''
5. Feche a conexão com o banco de dados.
'''
conexao.close()
'''
6. Utilize logging.info para registrar quando a tabela foi verificada/criada e quando a inserção do usuário foi finalizada.
'''
logging.info(f"A tabela foi criada às {tabela_criada}\nA inserção do usuário foi finalizada às {insercao_finalizada}")