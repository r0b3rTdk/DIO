'''
1. Crie uma função chamada coletar_e_salvar_usuario(id_usuario).
'''
import requests, json, sqlite3, logging

logging.basicConfig(level=logging.INFO)
def coletar_e_salvar_usuario(id_usuario): 
    '''
    2. Dentro da função, faça uma requisição GET para https://jsonplaceholder.typicode.com/users/{id_usuario} 
    (use f-string na URL para passar o ID dinamicamente).
    '''
    url = f"https://jsonplaceholder.typicode.com/users/{id_usuario}"
    resposta = requests.get(url)

    '''
    3. Use assert para garantir que a requisição foi bem-sucedida (status_code == 200).
    '''
    assert (resposta.status_code) == 200

    '''
    4. Extraia o id e o name da resposta JSON.
    '''
    dados = resposta.json()
    usuario_id = dados["id"]
    usuario_nome = dados["name"]

    '''
    5. Abra a conexão com o banco_usuarios.db.
    '''
    conexao = sqlite3.connect("banco_usuarios.db")
    cursor = conexao.cursor()

    '''
    6. Insira os dados extraídos na tabela usuarios utilizando a boa prática dos placeholders ?.
    '''
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id INT,
            nome TEXT
        )
    """)
    cursor.execute("INSERT INTO usuarios (id, nome) VALUES(?, ?)", (usuario_id, usuario_nome))

    '''
    7. Faça o commit, feche a conexão e utilize logging.info para registrar que o usuário foi salvo com sucesso 
    (incluindo o nome dele na mensagem).
    '''
    conexao.commit()
    conexao.close()
    logging.info(f"usuario salvo com sucesso {usuario_nome}")

'''
8. Fora da função, chame coletar_e_salvar_usuario(2) para testar o script com um novo usuário.
'''
coletar_e_salvar_usuario(2)