def somar(a=0, b=0, c=0):
    """
    -> faz a soma de 3 valores e mostra o resultado
    para a: primeiro valor
    para b: segundo valor
    para c: terceiro valor
    funcao criada por Robert
    """
    global s #faz o valor de s ser global no codigo
    s = a + b + c 
    return s
r1 = somar(8, 2)
r2 = somar(1)
r3 = somar()
r4 = somar(10, 20, 30)
print(f"os calculos deram {r1}, {r2}, {r3}, {r4}")