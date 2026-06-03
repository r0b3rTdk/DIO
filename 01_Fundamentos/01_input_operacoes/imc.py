nome = input("digite seu nome: ")
peso = float(input("digite seu peso: "))
altura = float(input("Digite sua altura em metros: ")) / 100

imc = peso / (altura * altura) 

print(f"Boas vindas {nome}, seu IMC é: {imc:.2f}") 