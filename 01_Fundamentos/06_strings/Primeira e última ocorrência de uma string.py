frase = input("digite a frase: ").upper().strip()
print(f"a letra A aparece {frase.count('A')} vezes na frase")
print(f"a letra a apareceu primeiro na posicao {frase.find('A')+1}")
print(f"a letra a apareceu primeiro na posicao {frase.rfind('A')+1}")