"""
1. Crie uma variável contendo uma string com o texto "   aPRendEndo pyThon   ".
"""
x = "   aPRendEndo pyThon   "

"""
2. Usando os métodos de string, remova os espaços em branco do início e do fim, 
e formate o texto para que apenas a primeira letra da frase fique maiúscula e o 
restante minúsculo (estilo "Title" ou Capitalizado).
"""
x = x.strip().title()

"""
3. Crie uma lista vazia chamada linguagens.
"""
linguagens = []

"""
4. Adicione o texto formatado no passo 2 dentro dessa lista.
"""
linguagens.append(x)

"""
5. Imprima uma mensagem usando f-string que diga: "O primeiro item da lista é: [item]",
substituindo [item] pelo valor que você guardou na lista.
"""
print(f"O primeiro item da lista é: {linguagens[0]}")