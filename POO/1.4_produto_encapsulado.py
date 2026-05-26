'''
1. Atualize a classe Produto, alterando o atributo de preço para ser protegido (_preco) dentro do __init__ e no método __str__.
'''

class Produto:
    
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco

    def __str__(self):
        return f"Produto: {self.nome}, Preço: R${self._preco}"
    
    '''
    2. Crie um método de instância chamado get_preco que apenas retorne o valor de _preco.
    '''
    def get_preco(self):
        return self._preco
    '''
    3. Crie um método de instância chamado set_preco que receba o parâmetro novo_valor. 
    Este método só deve atualizar o _preco se o novo_valor for maior que zero.
    '''
    def set_preco(self, novo_valor):
        if novo_valor > 0:
            self._preco = novo_valor

'''
4. Fora da classe, instancie um produto.
'''
objeto = Produto("teclado", 200)

print(objeto.nome, objeto._preco)

print(objeto)

'''
5. Tente alterar o preço chamando set_preco com um valor negativo (para testar a regra) e, 
em seguida, chame novamente com um valor positivo.
'''
objeto.set_preco(-10)
print(objeto)

objeto.set_preco(150)
print(objeto)

'''
6. Imprima o preço final do objeto chamando o método get_preco.
'''
print(objeto.get_preco())