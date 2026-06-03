quanti_18 = 0
homens = 0
mulher_20 = 0

while True:
    print("\nCADASTRE UMA PESSOA")
    print("-"*20)
    idade = int(input("\ndigite a sua idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input("\nqual o seu sexo? [M/F] ").strip().upper()[0]
    print("-"*20)

    if idade >= 18:
        quanti_18 += 1 
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher_20 += 1
    
    escolha = ' '
    while escolha not in 'SN':
        escolha = input("\nquer adicionar mais pessoas? [S/N] ").strip().upper()[0]
    if escolha == 'N':
        break

print(f""" 
      voce cadastrou: 
      {quanti_18} pessoas de maioridade
      {homens} homens
      {mulher_20} mulheres abaixo dos 20
      """)