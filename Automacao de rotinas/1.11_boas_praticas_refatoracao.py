def proc(l):
    r = []
    for x in l:
        if x > 0:
            r.append(x * 10)
    return r
'''
1. Refatore essa função dando a ela e aos seus parâmetros nomes claros e descritivos.
'''
def multiplicar_positivos_por_dez(lista):
    '''
    2. Substitua o loop for inteiro por uma única linha utilizando list comprehension 
    (que além de mais limpo, é mais rápido).
    '''
    resultado = [numero * 10 for numero in lista if numero > 0]
    return resultado 

'''
3. Fora da função, crie uma lista misturando números positivos e negativos, 
chame a sua função refatorada e exiba o resultado.
'''
lista = [10, -2, 40, 5, -4, -7, 2, 22, -6, 9, 11]
numero_pos_processamento = multiplicar_positivos_por_dez(lista)

print(f"numeros positivos vezes 10: {numero_pos_processamento}")