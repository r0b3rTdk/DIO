def aumentar(n, taxa):
    aumento = n + ( n * (taxa / 100))
    return aumento

def diminuir(n, taxa):
    reducao = n - ( n * (taxa / 100))
    return reducao

def dobro(n):
    d = n * 2
    return d

def metade(n):
    m = n / 2
    return m

def moeda(n):
    return f"R${n:.2f}".replace('.', ',')

def resumo(p, taxa, resp):
    titulo('RESUMO DO VALOR')
    txt(f"preco analisado: \t{moeda(p)}")
    txt(f"o dobro do preco: \t{moeda(dobro(p))}")
    txt(f"a metade do preco:  \t{moeda(metade(p))}")
    if resp == '0':
        txt(f"{taxa}% de reducao: \t{moeda(diminuir(p, taxa))}")
    else:
        txt(f"{taxa}% de aumento: \t{moeda(aumentar(p, taxa))}")
    print('-' * 35)  
    
def txt(msg):
    print(f"  {msg}")
    
def titulo(msg):
    tam = len(msg) + 20
    print('-' * tam)
    print(f"    {msg:>20}")
    print('-' * tam)
