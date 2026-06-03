# Importa o módulo sqlite3, que já vem instalado no Python
# Ele serve para criar e manipular bancos de dados leves (arquivos .db)
#
import sqlite3 as sql

class TransactionObject():
    """
    Classe responsável por gerenciar a conexão com o Banco de Dados.
    Ela abre a porta (connect), faz o trabalho (execute) e fecha a porta (disconnect).
    """
    # Nome do arquivo do banco de dados
    database = "clientes.db"
    conn = None # Variável para a conexão
    cur = None  # Variável para o cursor (quem executa os comandos)
    connected = False # Flag para saber se está conectado

    def connect(self):
        # Cria a conexão com o arquivo 'clientes.db'
        TransactionObject.conn = sql.connect(TransactionObject.database)
        # Cria o cursor (o objeto que percorre o banco e executa comandos)
        TransactionObject.cur = TransactionObject.conn.cursor()
        TransactionObject.connected = True

    def disconnect(self):
        # Fecha a conexão para liberar memória e salvar o arquivo
        TransactionObject.conn.close()
        TransactionObject.connected = False

    def execute(self, sql, parms=None):
        # Esta função executa os comandos SQL (INSERT, SELECT, UPDATE...)
        if TransactionObject.connected:
            if parms == None:
                # Se não houver parâmetros extras (ex: apenas um SELECT simples)
                TransactionObject.cur.execute(sql)
            else:
                # Se houver parâmetros (ex: dados do cliente para inserir), usa eles
                TransactionObject.cur.execute(sql, parms)
            return True
        else:
            return False

    def fetchall(self):
        # Recupera todas as linhas encontradas após um SELECT
        return TransactionObject.cur.fetchall()

    def persist(self):
        # O 'commit' é essencial! Ele confirma e salva as alterações no disco.
        # Sem isso, os dados seriam perdidos ao fechar o programa.
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        else:
            return False

# --- FUNÇÕES DO CRUD (Create, Read, Update, Delete) ---

def initDB():
    """
    Função inicial: Cria a tabela 'clientes' se ela ainda não existir.
    """
    trans = TransactionObject()
    trans.connect()
    # Comando SQL para criar a tabela com: ID, nome, sobrenome, email e cpf
    trans.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
    trans.persist()
    trans.disconnect()

def insert(nome, sobrenome, email, cpf):
    """
    Função para Inserir (Create) um novo cliente.
    """
    trans = TransactionObject()
    trans.connect()
    # INSERT INTO: comando para adicionar dados.
    # NULL é passado no ID para que o banco gere o número automaticamente.
    # Os '?' são substituídos pelas variáveis (nome, sobrenome...) por segurança.
    trans.execute("INSERT INTO clientes VALUES(NULL, ?,?,?,?)", (nome, sobrenome, email, cpf))
    trans.persist()
    trans.disconnect()

def view():
    """
    Função para Ler/Visualizar (Read) todos os clientes.
    """
    trans = TransactionObject()
    trans.connect()
    # SELECT *: seleciona TUDO da tabela clientes.
    trans.execute("SELECT * FROM clientes")
    rows = trans.fetchall() # Pega os resultados
    trans.disconnect()
    return rows # Retorna a lista de clientes para quem chamou a função

def search(nome="", sobrenome="", email="", cpf=""):
    """
    Função para Buscar clientes específicos.
    """
    trans = TransactionObject()
    trans.connect()
    # Busca por qualquer um dos campos (OR)
    trans.execute("SELECT * FROM clientes WHERE nome=? or sobrenome=? or email=? or cpf=?", (nome, sobrenome, email, cpf))
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def delete(id):
    """
    Função para Deletar (Delete) um cliente pelo ID.
    """
    trans = TransactionObject()
    trans.connect()
    # DELETE FROM: apaga a linha onde o id for igual ao informado.
    trans.execute("DELETE FROM clientes WHERE id = ?", (id,))
    trans.persist()
    trans.disconnect()

def update(id, nome, sobrenome, email, cpf):
    """
    Função para Atualizar (Update) os dados de um cliente existente.
    """
    trans = TransactionObject()
    trans.connect()
    # UPDATE: atualiza os campos SET ... WHERE id = ...
    trans.execute("UPDATE clientes SET nome =?, sobrenome=?, email=?, cpf=? WHERE id = ?", (nome, sobrenome, email, cpf, id))
    trans.persist()
    trans.disconnect()

# Executa a criação do banco assim que o arquivo for rodado
initDB()