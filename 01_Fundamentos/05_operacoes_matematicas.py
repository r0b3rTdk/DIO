numero1 = float(input("digite um numero: "))
numero2 = float(input("digite um numero: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multi = numero1 * numero2
divisao = numero1 / numero2
potencia = numero1 ** numero2
divisao_inteira = numero1 // numero2
resto = numero1 % numero2
ao_cubo = pow(numero1,numero2) #funcao interna de potencia
raiz_quadrada = numero1**(1/2) #raiz quadrada
raiz_cubica = numero2**(1/3)   #raiz cubica

print("=" * 20)
print(f"Os resultados são:")
print(f"Soma: {soma:^10}")           #deixa o resultado 10 casas centralizado
print(f"Subtração: {subtracao:<10}") #deixa o resultado 10 casas a esquerda
print(f"Multiplicação: {multi:>10}") #deixa o resultado 10 casas direita
print(f"Divisão: {divisao}")         
print(f"Potência: {potencia}")
print(f"Divisão inteira: {divisao_inteira}")
print(f"Resto da divisão: {resto}")
print(f"Raiz quadrada de {numero1}: {raiz_quadrada:.2f}") 
print(f"Raiz cúbica de {numero2}: {raiz_cubica:.2f}")
print("=" * 20)
