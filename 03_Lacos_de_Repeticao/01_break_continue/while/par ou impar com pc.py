import random

contador  = 0

while True:
    
    print("=-="*20)
    num_usuario = int(input("Digite um número: "))
    par_impar = input("escolha entre par ou impar? [P\I] ").strip().upper()[0]
    num_pc = random.randint(0, 10)        
    
    resultado = num_pc + num_usuario

    if par_impar == 'P':
        if resultado % 2 == 0:
            print("=-="*20)
            print(f"""\n
              voce escolheu {num_usuario} e o pc escolheu {num_pc}
                        deu PAR, VOCE GANHOU\n\n""")
            contador += 1
        else:
            print("=-="*20)
            print(f"""
              \n
              voce escolheu {num_usuario} e o pc escolheu {num_pc}
                        deu IMPAR, que azar, voce perdeu\n\n""")
            break
    else:
        if resultado % 2 == 0:
            print("=-="*20)
            print(f"""\n
              voce escolheu {num_usuario} e o pc escolheu {num_pc}
                        deu IMPAR, que azar, voce perdeu\n\n""")
            break
        else:
            print("=-="*20)
            print(f"""
              voce escolheu {num_usuario} e o pc escolheu {num_pc}
                        deu PAR, VOCE GANHOU\n\n""")
            contador += 1

if contador > 0:
    if contador == 1:
        print("=-="*20)
        print(f"\nvoce foi o ganhador {contador} vez")
    else:
        print("=-="*20)
        print(f"\nvoce foi o ganhador {contador} vezes")
else:
    print("=-="*20)
    print(f"\nque azar! voce perdeu na primeira")
    
    

