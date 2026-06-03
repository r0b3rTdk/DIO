def fatorial(num=1, show=False):
    '''
    -> calcula o fatorial de um numero
    podendo mostrar ou n o calculo com o 'show'
    '''
    f = 1
    print(f"\ncalculando {num}!...")
    for c in range(num, 0, -1):
        if show:
            if c > 1:
                print(f"{c} x ", end='')
            else:
                print(f"{c} = ", end='')
        f *= c
    return f
    
num = int(input("digite o numero: ")) 
mostrarCalculo = input("quer ver o calculo? [S/N] ").strip().upper()[0] 
while mostrarCalculo not in 'SN':
    mostrarCalculo = input("tente novamente... quer ver o calculo? [S/N] ").strip().upper()[0] 
if mostrarCalculo == 'S': 
    resultado = fatorial(num, show=True)
else:
    resultado = fatorial(num, show=False)

print(f"{resultado}")
help(fatorial)