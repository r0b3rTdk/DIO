from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase # Importa a classe do arquivo database.py

# Janela de Criação de Conta
class CreateAccountWindow(Screen):
    # Conecta com os ids do arquivo .kv
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        # Verifica se os campos não estão vazios e se o email parece válido
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                # Adiciona no banco de dados
                db.add_user(self.email.text, self.password.text, self.namee.text)
                self.reset()
                # Muda a tela para login
                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        # Limpa os campos de texto
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

# Janela de Login
class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        # Usa o banco de dados para validar senha
        if db.validate(self.email.text, self.password.text):
            # Salva quem é o usuário atual na classe MainWindow
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""

# Janela Principal (Pós-login)
class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = "" # Guarda o email do usuário logado

    def logOut(self):
        sm.current = "login"

    # Função chamada automaticamente quando a tela é exibida
    def on_enter(self, *args):
        # Busca os dados do usuário logado para exibir na tela
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created

# Gerenciador de Telas
class WindowManager(ScreenManager):
    pass

# Funções auxiliares para mostrar Popups de erro
def invalidLogin():
    pop = Popup(title='Invalid Login',
                content=Label(text='Invalid username or password.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()

def invalidForm():
    pop = Popup(title='Invalid Form',
                content=Label(text='Please fill in all inputs with valid information.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()

# Carrega o arquivo de interface visual
# ATENÇÃO: O nome do arquivo deve ser exatamente o que você salvou. Usei "mk.kv" conforme seu upload.
kv = Builder.load_file("mk.kv")

sm = WindowManager()
db = DataBase("users.txt")

# Cria as telas e adiciona ao gerenciador
screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"), MainWindow(name="main")]

for screen in screens:
    sm.add_widget(screen)

sm.current = "login"

class MyMainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MyMainApp().run()