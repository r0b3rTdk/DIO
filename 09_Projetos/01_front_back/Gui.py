# Importa todos os módulos da biblioteca tkinter (necessário para a interface gráfica)

from tkinter import *

class Gui():
    """
    Classe da Interface Gráfica
    Aqui definiremos toda a estrutura visual da aplicação.
    """
    # Definição de variáveis globais de espaçamento e largura
    x_pad = 5
    y_pad = 3
    width_entry = 30

    def __init__(self):
        # --- CRIAÇÃO DA JANELA ---
        # Cria a janela principal da aplicação
        self.window = Tk()
        
        # Define o título da janela (Nome fantasia da aplicação)
        self.window.wm_title("PYSQL versão 1.0")

        # --- DEFINIÇÃO DAS VARIÁVEIS DE DADOS ---
        # Essas variáveis especiais do Tkinter (StringVar) armazenam os textos digitados
        # nos campos de input. Elas fazem o 'bind' (ligação) com os campos.
        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtCPF = StringVar()

        # --- CRIAÇÃO DOS OBJETOS (WIDGETS) ---
        
        # Labels: São os textos fixos que indicam o que é cada campo (Nome, Sobrenome, etc.)
        self.lblnome = Label(self.window, text="Nome")
        self.lblsobrenome = Label(self.window, text="Sobrenome")
        self.lblemail = Label(self.window, text="Email")
        self.lblcpf = Label(self.window, text="CPF")

        # Entries: São as caixas de texto onde o usuário digita.
        # 'textvariable' liga a caixa à variável criada acima. 
        # 'width' define a largura da caixa.
        self.entNome = Entry(self.window, textvariable=self.txtNome, width=self.width_entry)
        self.entSobrenome = Entry(self.window, textvariable=self.txtSobrenome, width=self.width_entry)
        self.entEmail = Entry(self.window, textvariable=self.txtEmail, width=self.width_entry)
        self.entCPF = Entry(self.window, textvariable=self.txtCPF, width=self.width_entry)

        # Listbox: É a caixa grande à direita onde aparecerá a lista de clientes cadastrados.
        self.listClientes = Listbox(self.window, width=100)
        
        # Scrollbar: É a barra de rolagem lateral para a lista de clientes.
        self.scrollClientes = Scrollbar(self.window)

        # Buttons: São os botões de ação (Ver todos, Buscar, Inserir, etc.)
        self.btnViewAll = Button(self.window, text="Ver todos")
        self.btnBuscar = Button(self.window, text="Buscar")
        self.btnInserir = Button(self.window, text="Inserir")
        self.btnUpdate = Button(self.window, text="Atualizar Selecionados")
        self.btnDel = Button(self.window, text="Deletar Selecionados")
        self.btnClose = Button(self.window, text="Fechar")

        # --- ASSOCIANDO OS OBJETOS AO GRID (POSICIONAMENTO) ---
        
        # O .grid() organiza os elementos em linhas (row) e colunas (column).
        
        # Coluna 0 (Labels) e Coluna 1 (Inputs)
        self.lblnome.grid(row=0, column=0)
        self.entNome.grid(row=0, column=1)
        
        self.lblsobrenome.grid(row=1, column=0)
        self.entSobrenome.grid(row=1, column=1)
        
        self.lblemail.grid(row=2, column=0)
        self.entEmail.grid(row=2, column=1)
        
        self.lblcpf.grid(row=3, column=0)
        self.entCPF.grid(row=3, column=1)

        # Posicionamento da Lista e Scrollbar (Lado Direito)
        # rowspan=10 faz eles ocuparem a altura de 10 linhas para ficarem grandes
        self.listClientes.grid(row=0, column=2, rowspan=10)
        self.scrollClientes.grid(row=0, column=6, rowspan=10)

        # Posicionamento dos Botões (Abaixo dos campos de texto)
        # columnspan=2 faz o botão ocupar a largura de 2 colunas para ficar centralizado
        self.btnViewAll.grid(row=4, column=0, columnspan=2)
        self.btnBuscar.grid(row=5, column=0, columnspan=2)
        self.btnInserir.grid(row=6, column=0, columnspan=2)
        self.btnUpdate.grid(row=7, column=0, columnspan=2)
        self.btnDel.grid(row=8, column=0, columnspan=2)
        self.btnClose.grid(row=9, column=0, columnspan=2)

        # --- CONEXÃO DO SCROLLBAR COM A LISTBOX ---
        # Diz para a lista que, quando rolar, deve mexer na scrollbar vertical (y)
        self.listClientes.configure(yscrollcommand=self.scrollClientes.set)
        # Diz para a scrollbar que, quando mexer nela, deve rolar a lista (view)
        self.scrollClientes.configure(command=self.listClientes.yview)

        # --- ADICIONAR APARÊNCIA (SWAG) ---
        # Este loop percorre todos os filhos (widgets) da janela para aplicar estilo padrão
        for child in self.window.winfo_children():
            widget_class = child.__class__.__name__
            
            if widget_class == "Button":
                # Botões esticam horizontalmente (WE) e ganham preenchimento (pad)
                child.grid_configure(sticky='WE', padx=self.x_pad, pady=self.y_pad)
            
            elif widget_class == "Listbox":
                # Lista ganha preenchimento zero nas bordas
                child.grid_configure(padx=0, pady=0, sticky='NS')
            
            elif widget_class == "Scrollbar":
                # Scrollbar também ganha preenchimento zero
                child.grid_configure(padx=0, pady=0, sticky='NS')
            
            else:
                # Labels e Entries ganham preenchimento padrão e alinham à esquerda/direita
                child.grid_configure(padx=self.x_pad, pady=self.y_pad, sticky='N')

    # Método para rodar a aplicação
    def run(self):
        # O mainloop mantém a janela aberta e ouvindo cliques
        self.window.mainloop()

# --- EXECUÇÃO DO PROGRAMA ---
# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":
    app = Gui() # Instancia a classe
    app.run()   # Roda a janela