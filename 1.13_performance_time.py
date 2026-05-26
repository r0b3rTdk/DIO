'''
1. Importe a biblioteca nativa time.
'''
import time

'''
2. Crie uma lista gigante de números (ex: numeros = list(range(10_000_000))).
'''
numeros = list(range(10_000_000))

'''
3. Marque o tempo inicial usando inicio = time.time(). 
'''
inicio = time.time()

'''
4. Calcule a soma de todos os números da lista utilizando um loop for padrão. 
'''
total = 0
for numero in numeros:
    total += numero

'''
5. Marque o tempo final e calcule a duração da operação (fim - inicio). Imprima esse tempo. 
'''
print("Loop:", time.time() - inicio) 

'''
6. Repita o mesmo processo (marcar início, somar e marcar fim), mas agora utilizando a função nativa sum(numeros). 
'''
inicio = time.time()
sum(numeros)
print("sum()", time.time() - inicio)

'''
7. Imprima o tempo da função nativa para compararmos a diferença de performance.
'''