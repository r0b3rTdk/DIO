# Importa todas as ferramentas visuais do nosso arquivo Gui.py
from Gui import *
# Importa as funções de banco de dados do arquivo Backend.py e dá o apelido de "core"
import Backend as core

# Variável global para armazenar qual linha da lista está selecionada no momento
selected = None

def view_command():
    """
    Função para o botão 'Ver todos'.
    """
    # 1. Chama a função view() do Backend para pegar os dados do banco
    rows = core.view()
    
    # 2. Limpa a lista visual da tela (do índice 0 até o final)
    app.listClientes.delete(0, END)
    
    # 3. Insere cada linha encontrada no banco dentro da lista visual
    for r in rows:
        app.listClientes.insert(END, r)

def search_command():
    """
    Função para o botão 'Buscar'.
    """
    app.listClientes.delete(0, END)
    # Pega o que está escrito nas caixas de texto (.get()) e manda para a busca do Backend
    rows = core.search(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    for r in rows:
        app.listClientes.insert(END, r)

def insert_command():
    """
    Função para o botão 'Inserir'.
    """
    # Manda os dados digitados para o Backend salvar
    core.insert(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    # Atualiza a lista para mostrar o novo registro
    view_command()

def getSelectedRow(event):
    """
    Função mágica que preenche os campos quando clicamos em um nome na lista.
    """
    global selected
    try:
        # Pega o índice da linha clicada na lista visual
        index = app.listClientes.curselection()[0]
        # Pega os dados completos daquela linha (ID, Nome, Sobrenome...)
        selected = app.listClientes.get(index)
        
        # Limpa os campos de texto
        app.entNome.delete(0, END)
        app.entSobrenome.delete(0, END)
        app.entEmail.delete(0, END)
        app.entCPF.delete(0, END)
        
        # Preenche os campos com os dados do cliente selecionado
        # selected[1] é o nome, selected[2] sobrenome, etc. (O [0] é o ID)
        app.entNome.insert(END, selected[1])
        app.entSobrenome.insert(END, selected[2])
        app.entEmail.insert(END, selected[3])
        app.entCPF.insert(END, selected[4])
        
        return selected
    except IndexError:
        pass # Se clicar numa área vazia, não faz nada

def update_command():
    """
    Função para o botão 'Atualizar'.
    """
    # Usa o ID do cliente selecionado (selected[0]) e os novos textos digitados para atualizar
    if selected:
        core.update(selected[0], app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
        view_command()

def del_command():
    """
    Função para o botão 'Deletar'.
    """
    if selected:
        # Pega o ID (selected[0]) e manda o Backend apagar
        id = selected[0]
        core.delete(id)
        view_command()

# --- INÍCIO DO PROGRAMA ---
if __name__ == "__main__":
    # 1. Carrega a Interface Gráfica
    app = Gui()
    
    # 2. Conecta a Lista Visual à função de clique (bind)
    # Quando houver um evento de seleção na lista ('<<ListboxSelect>>'), chama getSelectedRow
    app.listClientes.bind('<<ListboxSelect>>', getSelectedRow)
    
    # 3. Conecta os Botões às suas Funções (Comandos)
    app.btnViewAll.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)
    
    # 4. Roda a aplicação
    app.run()