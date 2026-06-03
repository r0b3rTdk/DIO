sexo = input("Digite o seu sexo (M/F): ").strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    print("Valor inválido! Por favor, digite novamente.")
    sexo = input("Digite o seu sexo (M/F): ").upper()
if sexo == 'M':
    print("Sexo Masculino registrado com sucesso!")
if sexo == 'F':
    print("Sexo Feminino registrado com sucesso!")

