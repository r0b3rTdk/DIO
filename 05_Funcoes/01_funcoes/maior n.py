def maior(*num):
    if len(num) == 0:
        print("Nenhum valor foi informado.")
        return
    
    maior = num[0]
    
    for valor in num:
        if valor > maior:
            maior = valor
    
    print(f"{num}", end=' ')
    print(f"foram informados {len(num)} valores")
    print(f"o maior valor informado foi: {maior}")

valores = [3, 5, 6, 7]
maior(*valores)
valores = [7, 99, 26, 37]
maior(*valores)
valores = [0, 4, 2]
maior(*valores)
valores = [3, 55]
maior(*valores)
valores = [53, 77, 96, 70, 40]
maior(*valores)