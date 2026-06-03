import random

num_pc = random.randint(0, 10)  # O computador escolhe um número aleatório
print("-=-" * 20)
num_usuario = int(input("Digite um número entre 0 e 10. tente adivinha... "))  # O usuário tenta adivinhar
print("-=-" * 20)
palpites = 0

while num_pc != num_usuario:
    num_usuario = int(input("vc errou, tente novamente um numero entre 0 e 10. "))  # O usuário tenta adivinhar
    print("-=-" * 20)
    palpites += 1

print(f"acertou, parabens, vc precisou de {palpites} palpites pra acertar o numero escolhido pelo pc que era {num_pc}")
