def leiaNum(msg):
    
    while True:
        try:
            num = int(input(msg))  # Tenta converter a entrada para inteiro
            return num  # Retorna o número se for válido
        except ValueError:
            print("\033[0;31mErro! Por favor, digite um número inteiro válido.\033[m")

n = leiaNum("digite um numero: ")
print(f"voce digitou o numero {n}")
'''
Se não houver erro, o código dentro do bloco try será executado normalmente, e o except será ignorado.
Se houver um erro, a execução do programa pula para o bloco except
'''