velocidade = float(input("digite a velocidade do carro: "))

if velocidade > 80.0:
    multa = 5.0 * (velocidade - 80.0)
    print(f"voce foi multado, a multa e de: {multa}")
if velocidade < 80.0:
    print("voce esta dirigindo certo")
