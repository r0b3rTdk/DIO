'''
1. Crie uma classe base Funcionario com os atributos protegidos _nome e _salario_base.
'''
class Funcionario:
    def __init__(self, _nome, _salario_base):
        self._nome = _nome
        self._salario_base = _salario_base
    '''
    2. Na classe Funcionario, crie um método calcular_salario() que retorne o _salario_base.
    '''
    def calcular_salario(self):
        return self._salario_base

    '''
    3. Ainda na classe Funcionario, implemente o método especial __str__ para retornar exatamente o formato: 
    "Nome: <nome> - Salário Final: R$<salario_calculado>". Repare que você deve chamar o método calcular_salario() aqui dentro.
    '''
    def __str__(self):
        return f"Nome: {self._nome} - Salário Final: R${self.calcular_salario()}"

'''
4. Crie uma classe filha Desenvolvedor que herde de Funcionario. 
O seu construtor deve receber nome, salário base e linguagem. Use o super() adequadamente.
'''
class Desenvolvedor(Funcionario):
    def __init__(self, _nome, _salario_base, linguagem):
        super().__init__(_nome, _salario_base)
        self.linguagem = linguagem

'''
5. Crie uma classe filha Gerente que também herde de Funcionario. O construtor recebe apenas nome e salário base. 
Dentro do construtor, inicialize um atributo protegido _equipe como uma lista vazia.
'''
class Gerente(Funcionario):
    def __init__(self, _nome, _salario_base):
        super().__init__(_nome, _salario_base)
        self._equipe = []

    '''
    6. Na classe Gerente, crie um método adicionar_dev(desenvolvedor) que inclua um objeto da 
    classe Desenvolvedor na lista _equipe.
    '''
    def adicionar_dev(self, desenvolvedor):
        self._equipe.append(desenvolvedor)

    '''
    7. Aplique o polimorfismo: sobrescreva o método calcular_salario() dentro da classe Gerente. O salário de um gerente 
    deve ser o _salario_base mais um bônus de 10% do _salario_base para cada desenvolvedor que ele tiver na sua equipe.
    '''
    def calcular_salario(self):
            bonus_unitario = self._salario_base * (10 / 100)
            bonus_total = bonus_unitario * len(self._equipe)
            return self._salario_base + bonus_total

'''
8. Fora das classes, instancie dois desenvolvedores e um gerente. Adicione os dois desenvolvedores à equipe do gerente. 
Por fim, chame o print() para exibir as informações dos três funcionários.
'''
desenvolvedores1 = Desenvolvedor("r0b3rT", 4000, "Python")
desenvolvedores2 = Desenvolvedor("r3n4n", 2000, "C")
gerente = Gerente("Celio", 6000)

gerente.adicionar_dev(desenvolvedores1)
gerente.adicionar_dev(desenvolvedores2)

print(desenvolvedores1)
print(desenvolvedores2)
print(gerente)