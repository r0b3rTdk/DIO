n = 0
contador = 0
soma = 0

while True:
    n = int(input("digite um numero: "))
    if n == 999:
        break

    contador += 1
    soma += n
    
media = soma / contador
print(f"""
      vc digitou {contador} numeros
      a soma desses numeros deu {soma}
      e a media foi de {media:.2f}
      """)