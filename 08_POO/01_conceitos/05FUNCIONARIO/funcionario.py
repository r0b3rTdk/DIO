class Funcionario:
    
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        # Dicionários (Hashtables):
        # Aqui a mágica acontece. Em vez de uma variável para guardar 'horas',
        # criamos um dicionário vazio {}. Isso permite guardar pares de Chave:Valor.
        # Exemplo futuro: {'Jan': 300, 'Fev': 200}
        self.horas = {}
        self.salario_hora = {}
    
    def cadastro_hora(self, mes, horas):
        # Validação de Chave:
        # Só adicionamos se o mês (a chave) ainda não existir no dicionário.
        # Isso evita que você sobrescreva acidentalmente um mês já fechado.
        if (mes not in self.horas):
            self.horas[mes] = horas
    
    def cadastro_salario_hora(self, mes, valor):
        # Mesma lógica acima. 
        # Isso permite que o salário varie mês a mês (aumentos, horas extras valendo mais, etc).
        if (mes not in self.salario_hora):
            self.salario_hora[mes] = valor
    
    def calcula_salario(self, mes):
        # Lógica de Dependência:
        # Para calcular, precisamos ter dados nos DOIS dicionários para aquele mês específico.
        if (mes not in self.horas) or (mes not in self.salario_hora):
            print("Mês inexistente")
        else: return self.horas[mes] * self.salario_hora[mes]
    
    # __repr__ (Representação Oficial):
    # Diferente do __str__ (que é para ficar bonito pro usuário), o __repr__ 
    # serve para mostrar como o objeto é "por dentro", útil para programadores (debugging).
    # Quando você der print no objeto, ele mostrará o estado atual dos dicionários.
    def __repr__(self):
        return f'Funcionario: {self.nome}, \nEmail: {self.email}, \nHoras/Mes: {self.horas}, \nSalário por hora: {self.salario_hora}'
        