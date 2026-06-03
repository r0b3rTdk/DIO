numero_1 = float(input("digite o primeiro numero: "))
numero_2 = float(input("digite o segundo numero: "))
print("1 - + soma")
print("2 - - subtracao")
print("3 - * multiplicacao")
print("4 - / divisao")
operacao = int(input("qual a operacao vc deseja? "))

if operacao == 1:
    resultado = numero_1 + numero_2
    print(resultado)
elif operacao == 2:
    resultado = numero_1 - numero_2
    print(resultado)   
elif operacao == 3:
    resultado = numero_1 * numero_2
    print(resultado)   
elif operacao == 4:
    resultado = numero_1 / numero_2
    print(resultado)   
else:
    print("digite uma operacao valida, entre 1 e 4")