num1 = int(input("digite o primeiro valor: "))
num2 = int(input("digite o segundo valor: "))
escolha = int(input("""
      Menu de Operacoes
      [1] somar
      [2] multiplicar
      [3] maior
      [4] novos numeros
      [5] sair do programa
      digite sua escolha [1/5]: """))
while escolha != 5:
    if escolha == 1:
        print(f"a soma entre {num1} e o {num2} = {num1+num2}")
    if escolha == 2:
        print(f"a multiplicacao entre {num1} e o {num2} = {num1*num2}")
    if escolha == 3:
        maior = num1
        if maior < num2:
            maior = num2
            print(f"o maior entre {num1} e o {num2} = {maior}, que e o segundo numero")
        else:
            print(f"o maior entre {num1} e o {num2} = {maior}, que e o primeiro numero")
    if escolha == 4:
        num1 = int(input("digite o novo primeiro numero: "))
        num2 = int(input("digite o novo segundo numero: "))
    
    escolha = int(input("""
      Menu de Operacoes
      [1] somar
      [2] multiplicar
      [3] maior
      [4] novos numeros
      [5] sair do programa
      digite sua escolha [1/5]: """))
print("acabou")