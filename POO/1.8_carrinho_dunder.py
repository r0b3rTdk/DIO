'''
1. Crie uma classe chamada Carrinho cujo método __init__ apenas inicialize um atributo protegido _produtos 
como uma lista vazia [].
'''
class Carrinho:
    def __init__(self):
        self._produtos = []

    '''
    2. Crie um método de instância chamado adicionar que receba um produto (string) e o inclua na lista _produtos.
    '''
    def adicionar(self, produto):
        self._produtos.append(produto)

    '''
    3. Implemente o método especial __len__ para retornar a quantidade de itens armazenados na lista _produtos do carrinho.
    '''
    def __len__(self):
        return len(self._produtos)

    '''
    4. Implemente o método especial __add__ recebendo os parâmetros self e outro. Este método deve criar um novo objeto da 
    classe Carrinho, juntar os produtos do self._produtos com os do outro._produtos dentro desse novo carrinho, e então retorná-lo.
    '''
    def __add__(self, outro):
        carrinho_novo = Carrinho()
        carrinho_novo._produtos = self._produtos + outro._produtos
        return carrinho_novo


'''
5. Fora da classe, instancie dois carrinhos diferentes (carrinho1 e carrinho2) e adicione alguns produtos a 
cada um usando o método adicionar.
'''
carrinho1 = Carrinho()
carrinho2 = Carrinho()

carrinho1.adicionar("teclado")
carrinho1.adicionar("gabinete")
carrinho1.adicionar("headset")
carrinho1.adicionar("mouse")

carrinho2.adicionar("placa_video")
carrinho2.adicionar("placa_mae")
carrinho2.adicionar("ram")
carrinho2.adicionar("fonte")

'''
6. Crie um carrinho3 somando os dois primeiros diretamente com o sinal de mais (ex: carrinho3 = carrinho1 + carrinho2).
'''
carrinho3 = carrinho1 + carrinho2

'''
7. Imprima na tela a quantidade de produtos do carrinho3 usando a função nativa do Python (ex: print(len(carrinho3))).
'''
print(len(carrinho3))