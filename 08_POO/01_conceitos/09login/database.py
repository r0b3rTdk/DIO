import datetime

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()
        
    def load(self):
        # Tenta abrir o arquivo de usuários para leitura
        try:
            self.file = open(self.filename, "r")
            self.users = {}
            
            for line in self.file:
                # Lê cada linha: email;senha;nome;data
                email, password, name, created = line.strip().split(";")
                self.users[email] = (password, name, created)
            
            self.file.close()
        except FileNotFoundError:
            # Se o arquivo não existir, cria um dicionário vazio
            self.users = {}
            
    def get_user(self, email):
        # Verifica se o email existe no "banco"
        if email in self.users:
            return self.users[email]
        else:
            return -1
        
    def add_user(self, email, password, name):
        # Adiciona um novo usuário se o email não existir
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("Email já cadastrado!")
            return -1
        
    def validate(self, email, password):
        # Valida se o email existe e a senha bate
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False
    
    def save(self):
        # Salva o dicionário de usuários de volta no arquivo de texto
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")
    
    @staticmethod
    def get_date():
        # Pega a data atual
        return str(datetime.datetime.now()).split(" ")[0]