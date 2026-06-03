import random

num_pc = random.randint(0, 5)  # O computador escolhe um número aleatório
print("-=-" * 20)
num_usuario = int(input("Digite um número entre 0 e 5. tente adivinha... "))  # O usuário tenta adivinhar
print("-=-" * 20)

if num_usuario == num_pc:
    print("Parabéns, você acertou! O número era:", num_pc)
else:
    print("Que pena, você errou. O número era:", num_pc)