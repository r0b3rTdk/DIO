# DEFINICAO DA CLASSE (O MOLDE)
class Pessoa:
    "Isto e uma classe nova chamada Pessoa" # a docstring
    idade = 15 # uma caracteristica que todos os objetos criados terao
    
    
    # Metodo e uma funcao que pertence a classe
    # o parametro self e obrigatorio e representa o objeto(instancia) que esta chamando o metodo
    def saudacao(self):
        print("Ola pessoa")
        
# Criando o objeto (INSTANCIACAO)
# aqui Matheus e um objeto da classe Pessoa
matheus = Pessoa()

#acessando atributos
# Exibe o valor guardado na variavel idade do objeto matheus 
print(matheus.idade)

# Referencia ao metodo vs execucao
# aqui voce apenas aponta para o metodo, nao para a roda.
print(matheus.saudacao)

# aqui voce esta executando o metodo
matheus.saudacao()

# Acessando a documentacao da classe
print(matheus.__doc__)