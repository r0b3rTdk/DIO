'''
1. Aproveite a classe Produto atual.
'''
class Produto:
    
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    '''
    2. Adicione a ela o método especial __str__.
    '''
    def __str__(self):
        '''
        3. Este método deve retornar uma string amigável que descreva o objeto. O formato deve ser exatamente este: "Produto: <nome do produto>, Preço: R$ <preco do produto>".
        '''
        return f"Produto: {self.nome}, Preço: R${self.preco}"
objeto = Produto("teclado", 200)

print(objeto.nome, objeto.preco)

'''
4. Fora da classe, instancie o produto e chame a função print() passando o próprio objeto diretamente (ex: print(objeto)).
'''
print(objeto)