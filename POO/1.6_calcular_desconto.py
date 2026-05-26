'''
1. Mantenha a classe base Produto e a classe filha Eletronico (com o uso do super()).
'''
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    '''
    3. Na classe base Produto, adicione um método de instância chamado calcular_desconto que calcule e 
    retorne um desconto padrão de 5% sobre o preço.
    '''
    def calcular_desconto(self):
        desconto = self.preco * (5 / 100)
        return self.preco - desconto

class Eletronico(Produto):

    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.voltagem = voltagem
        '''
        4. Aplique o polimorfismo: sobrescreva (recrie) o método calcular_desconto dentro da classe Eletronico 
        para retornar um desconto de 10%.
        '''
    def calcular_desconto(self):
        desconto = self.preco * (10 / 100)
        return self.preco - desconto
'''
2. Crie uma nova classe filha chamada Alimento que também herde de Produto. 
O __init__ dela deve receber nome, preco e data_validade, usando o super() da mesma forma que você fez antes.
'''
class Alimento(Produto):
    def __init__(self, nome, preco, data_validade):
        super().__init__(nome, preco)
        self.data_validade = data_validade

    '''
    5. Sobrescreva também o método calcular_desconto na classe Alimento para retornar um desconto de 20%.
    '''
    def calcular_desconto(self):
        desconto = self.preco * (20 / 100)
        return self.preco - desconto

'''
6. Fora das classes, instancie um objeto de Eletronico e um objeto de Alimento.
'''
objetoEletronico = Eletronico("ventilador", 500, "Bivolt")
print(objetoEletronico.nome, objetoEletronico.preco, objetoEletronico.voltagem)

objetoAlimento = Alimento("Pizza", 110, 20)
print(objetoAlimento.nome, objetoAlimento.preco, objetoAlimento.data_validade)

'''
7. Imprima o resultado de calcular_desconto() para os dois objetos criados, provando que o mesmo método 
gera resultados diferentes dependendo da classe.
'''
print(objetoEletronico.calcular_desconto())
print(objetoAlimento.calcular_desconto())