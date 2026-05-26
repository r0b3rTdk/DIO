'''
1. Crie uma classe chamada Produto com um atributo de classe (declarado fora do __init__) 
chamado taxa_imposto valendo 0.10 (que representa 10%).
'''
class Produto:
    taxa_imposto = 0.10
    '''
    2. Crie o método __init__ normalmente, recebendo e inicializando nome e preco. 
    '''
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    '''
    3. Crie um método de classe usando o decorador @classmethod chamado alterar_taxa que receba os parâmetros cls e nova_taxa. 
    Dentro do método, altere a variável da classe usando cls.taxa_imposto = nova_taxa.
    '''
    @classmethod
    def alterar_taxa(cls, nova_taxa):
        cls.taxa_imposto = nova_taxa

    '''
    4. Crie um método estático usando o decorador @staticmethod chamado gerar_codigo_barras que não recebe self nem cls. 
    Este método deve apenas retornar uma string fixa, como "123456789".
    '''
    @staticmethod
    def gerar_codigo_barras():
        return "123456789"

'''
5. Fora da classe, sem instanciar nenhum objeto, chame o método alterar_taxa diretamente pela classe 
(ex: Produto.alterar_taxa(...)) para alterar a taxa para 0.15.
'''
Produto.alterar_taxa(0.15)

'''
6. Em seguida, ainda usando apenas o nome da classe, imprima na tela o resultado de gerar_codigo_barras() 
e o novo valor do atributo de classe taxa_imposto para provar que a alteração funcionou.
'''
print(Produto.gerar_codigo_barras(), Produto.taxa_imposto)