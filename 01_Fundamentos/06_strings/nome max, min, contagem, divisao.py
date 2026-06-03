nome = input("Digite seu nome completo: ")

nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
numero_total_letras = len(nome)
primeiro_nome = nome.split()[0]
numero_letras_primeiro_nome = len(primeiro_nome)

print("Nome em maiúsculas:", nome_maiusculo)
print("Nome em minúsculas:", nome_minusculo)
print("Número total de letras:", numero_total_letras)
print("Número de letras do primeiro nome:", numero_letras_primeiro_nome)