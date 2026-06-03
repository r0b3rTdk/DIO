n = int(input("digite o numero: "))

soma = 0
media = 0
maior = n
menor = n
contador = 1

escolha = input("vc quer continuar a digitar novos numeros? [S/N]").upper()

while escolha == 'S':
    
    n = int(input("digite o numero: "))
    contador += 1
    soma += n
    if n > maior:
            maior = n
    if n < menor:
            menor = n
    escolha = input("vc quer continuar a digitar novos numeros? [S/N]").upper()

media = soma / contador

print(f"a media de todos os {contador} numeros digitados foi de {media}")
print(f"o maior numero foi {maior} e o menor foi {menor}")