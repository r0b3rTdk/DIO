def notas(* nota, sit = False):
    """
    -> faz o calculo de varias notas e retorna a media
    podendo retornar a situacao a depender do usuario
    funcao criada por Robert
    """
    sala = {}
    sala['total'] = len(nota)
    sala['maior'] = max(nota)
    sala['menor'] = min(nota)
    sala['media'] = sum(nota)/len(nota)
    if sit:
        if sala['media'] >= 7:
            sala['situacao'] = 'BOA'
        elif sala['media'] >= 5:
            sala['situacao'] = 'RAZOAVEL'
        else:
            sala['situacao'] = 'RUIM'
    return sala

resp = notas(7.5, 7.5, 9, 6.8, sit=True)
print(resp)
help(notas)