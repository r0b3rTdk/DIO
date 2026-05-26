'''
1. Crie uma classe base chamada Produto com o método __init__ recebendo e inicializando nome e preco.
'''
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
'''
2. Crie uma nova classe chamada Eletronico que herde da classe Produto.
'''
class Eletronico(Produto):

    '''
    3. No __init__ da classe Eletronico, você deve receber os parâmetros nome, 
    preco e um novo parâmetro chamado voltagem (ex: "110v" ou "Bivolt").
    '''
    def __init__(self, nome, preco, voltagem):
        '''
        4. Dentro desse __init__ do Eletronico, use super().__init__(...) para enviar o nome e o preco para a 
        classe pai inicializar. Logo abaixo, inicialize o atributo de instância voltagem na própria classe filha.
        '''
        super().__init__(nome, preco)
        self.voltagem = voltagem

'''
5. Fora da classe, instancie um objeto da classe Eletronico passando os 3 valores, 
e imprima na tela o nome, preço e voltagem do objeto criado.
'''
objeto = Eletronico("ventilador", 500, "Bivolt")
print(objeto.nome, objeto.preco, objeto.voltagem)