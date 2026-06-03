matriz = [[], [], []]

print(f'{"MATRIZ":^30}')
for i in range(0 , 3):
    print("""
           0 _|_|_
           1 _|_|_
           2 _|_|_
             0 1 2
          """)
    valor = int(input(f"digite o valor da matriz [{0}/{i}]: "))
    matriz[0].append(valor)
for i in range(0 , 3):
    print("""
           0 _|_|_
           1 _|_|_
           2 _|_|_
             0 1 2
          """)
    valor = int(input(f"digite o valor da matriz [{1}/{i}]: "))
    matriz[1].append(valor)
for i in range(0 , 3):
    print("""
           0 _|_|_
           1 _|_|_
           2 _|_|_
             0 1 2
          """)
    valor = int(input(f"digite o valor da matriz [{2}/{i}]: "))
    matriz[2].append(valor)

print(f"""
           0 {matriz[0][0]}|{matriz[0][1]}|{matriz[0][2]}
           1 {matriz[1][0]}|{matriz[1][1]}|{matriz[1][2]}
           2 {matriz[2][0]}|{matriz[2][1]}|{matriz[2][2]}
             0 1 2
          """)

par = 0
impar = 0
soma_par = 0
soma_impar = 0
for linha in matriz:
    for numero in linha:
        if numero % 2 == 0:
            par += 1
            soma_par += numero
        else:
            impar +=1
            soma_impar += numero
print(f"Número par encontrado: {par}")
print(f"Número impar encontrado: {impar}")

soma = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f"a soma da terceira coluna foi: {soma}")

maior = max(matriz[1])
print(f"o maior numero da segunda linha foi: {maior}")
'''
for linha in matriz:

Aqui, a variável linha vai representar uma das linhas da matriz em cada repetição do laço. A matriz é uma lista de listas (uma lista dentro da outra), e cada uma dessas "listas internas" é uma linha da matriz.
A matriz está estruturada assim:

matriz = [
    [1, 2, 3],  # linha 0
    [4, 5, 6],  # linha 1
    [7, 8, 9]   # linha 2
]
Então, no primeiro ciclo do for, a linha será a primeira linha da matriz, ou seja, [1, 2, 3]. No segundo ciclo, será a segunda linha [4, 5, 6], e assim por diante.
for numero in linha:

Aqui, o laço vai passar por cada número individual dentro de uma linha da matriz.
Por exemplo, se a linha for [1, 2, 3], a variável numero vai passar a ser o valor de cada item dessa lista, ou seja, primeiro 1, depois 2 e depois 3.

'''