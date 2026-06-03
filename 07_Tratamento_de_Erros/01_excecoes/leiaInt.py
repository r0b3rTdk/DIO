def leiaInt(msg):
    while True:
        try:
            num = int(input(msg)) 
            return num  
        except (ValueError, TypeError):
            print("\033[0;031mvoce nao digitou um numero inteiro\033[m")

def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
            return num
        except (ValueError, TypeError):
            print("\033[0;31mvoce nao digitou um numero real\033[m")

n = leiaInt("digite um numero: ")
f = leiaFloat("digite um numero real: ")
print(f"voce digitou o numero {n} e o real {f}")
    

