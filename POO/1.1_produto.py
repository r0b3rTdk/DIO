'''
1. Crie uma classe chamada Produto.
'''
class Produto:
    '''
    2. Defina o método construtor (__init__) para receber e inicializar dois atributos: nome (string) e preco (float).
    '''
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

'''
3. Fora da classe, instancie (crie) um objeto dessa classe passando os valores que você quiser para nome e preço.
'''
objeto = Produto("teclado", 200)
'''
4. Imprima na tela os atributos do objeto criado usando a notação de ponto (ex: objeto.atributo).
'''
print(objeto.nome, objeto.preco)