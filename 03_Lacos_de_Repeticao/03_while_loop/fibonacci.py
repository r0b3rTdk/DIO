n = int(input("Digite o numero inteiro: "))

print(f"Os {n} primeiros elementos da sequencia de fibonacci:")
a = 0
b = 1
contador = 1
while contador <= n:
    print(a, end= ' ')  # Exibe o termo atual
    soma = a + b  # Calcula o próximo termo
    a = b  # Atualiza `a` para o próximo valor na sequência
    b = soma  # Atualiza `b` para o valor do próximo termo
    contador += 1  # Incrementa o contador para não entrar em loop infinito
print("\nFim")