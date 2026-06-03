class Main:
    pass

print("Testando o projeto de POO")

from Cliente import Cliente

from Conta import Conta

c1= Cliente("Ana", 25)
conta=Conta(c1.get_nome(), 6565)

conta.deposita(500)
conta.saque(50)
conta.extrato()
