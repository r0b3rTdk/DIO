import time # Importa a biblioteca para controlar o tempo (pausas)
import os # Importa a biblioteca para dar comandos ao Sistema Operacional

class Cronometro:
    
    # 1. PARÂMETROS COM VALOR PADRÃO (Default Arguments)
    # Ao colocar '= 0', você torna esses parâmetros opcionais.
    # Você pode criar:
    # Cronometro() -> começa em 00:00:00
    # Cronometro(0, 30) -> começa em 00:30:00
    def __init__(self, segundos = 0, minutos = 0, horas = 0):
        self.segundos = segundos
        self.minutos = minutos
        self.horas = horas
     
    def __repr__(self):
        # 2. FORMATAÇÃO DE DADOS (:02d)
        # Essa é a forma profissional de formatar números em relógios.
        # :d -> diz que é um número inteiro (digit).
        # 02 -> diz para ocupar 2 casas e preencher com ZERO à esquerda se sobrar espaço.
        # Exemplo: 5 vira "05", 10 vira "10".
        return f'{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}'
    
    def incremento(self):
        # 3. LÓGICA DE CASCATA (Carry Over)
        # É a lógica mecânica do relógio. Quando uma unidade enche, ela transborda para a próxima.
        self.segundos += 1
        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1
        if self.minutos >= 60:
            self.minutos = 0
            self.horas += 1
    
    def start(self):
        # 4. O LOOP INFINITO (Game Loop / Main Loop)
        # A maioria dos programas interativos roda dentro de um 'while True'.
        while True:
            # Limpa o terminal para dar a ilusão de que os números estão mudando no lugar,
            # em vez de imprimir uma lista infinita de horários um embaixo do outro.
            # OBS: 'cls' é para Windows. Se estiver no Linux ou Mac, seria 'clear'.
            os.system('cls')
            # Chama o __repr__ e desenha o relógio
            print(self)
            self.incremento()
            time.sleep(1)
            
cronometro1 = Cronometro()

# O código entra no loop aqui e nunca mais sai (até você forçar a parada com Ctrl+C)
cronometro1.start()