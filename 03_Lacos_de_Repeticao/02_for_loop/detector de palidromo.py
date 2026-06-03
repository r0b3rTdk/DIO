frase = input("digite seu nome: ").strip().upper()
dividido = frase.split()
junto = ''.join(dividido)
inverso = ''
# inverso = junto[::-1] tambem pode ser feito assim
for letras in range(len(junto) - 1, -1, -1):
    inverso += junto[letras]
print(f"o inverso de {junto} e {inverso}")
if junto == inverso:
    print("temos um palindromo")
else:
    print("nao e um palindromo")
