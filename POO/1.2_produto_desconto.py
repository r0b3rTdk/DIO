'''
1. Aproveite a classe Produto que você acabou de criar e adicione a ela um método de instância chamado aplicar_desconto.
'''
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    '''
    2. Esse método deve receber, além do self, um parâmetro chamado percentual (um número como 10, representando 10%).
    '''
    def aplicar_desconto(self, percentual):
        '''
        3. Dentro do método, calcule o desconto e atualize o atributo preco do próprio objeto subtraindo o valor do desconto.
        '''
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto


objeto = Produto("teclado", 200)
'''
4. Fora da classe, instancie o produto, imprima o preço original, chame o método aplicar_desconto informando uma porcentagem e, por fim, imprima o novo preço atualizado.
'''
print(f"preco original = {objeto.preco}")

objeto.aplicar_desconto(10)
print(f"preco com desconto = {objeto.preco}")
