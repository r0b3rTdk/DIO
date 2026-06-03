class Conta:
    def __init__(self, titular, numero, saldo):
        
        self.saldo = 0
        self.numero = numero
        self.titular = titular
        
        @property
        def saldo(self):
            return self._saldo
        
        @saldo
        def saque(self, saldo):
            if (saldo<0):
                print("Saldo nao pode ser negativo")
            else:
                self._saldo = saldo
        
        @saque
        def saque(self, valor):
            if (self.saldo>=valor):
                self.saldo-=valor
                print("Saque realizado com sucesso")
            else:
                print("Saldo insuficiente")
        
        @deposita
        def deposita(self, valor):
            self.saldo+=valor
        
        @extrato
        def extrato(self):
            print("Cliente: ", self._titular, " Sado Atual: ", self._saldo)
                
        