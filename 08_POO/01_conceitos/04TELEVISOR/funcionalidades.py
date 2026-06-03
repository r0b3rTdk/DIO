class Televisor:
    def __init__(self, fab, modelo):
        self.fabricante = fab
        self.modelo = modelo
        self.canal_atual = None # Começa desligada/sem canal
        self.lista_de_canais = []
        self.volume = 20
        
    def aumentaVolume(self, valor):
        if self.volume+ valor <= 100:
            self.volume += valor
        else:
            self.volume = 100
    
    def diminuiVolume(self, valor):
        if self.volume - valor >= 0:
            self.volume-= valor
        else:
            self.volume = 0
    
    def trocaCanal(self, canal):
        # Só troca se o canal já tiver sido sintonizado antes
        if canal in self.lista_de_canais:
            self.canal_atual = canal
    
    def sintonizaCanal(self, canal):
        # Adiciona o canal na lista se ele ainda não estiver lá (evita duplicados)
        if canal not in self.lista_de_canais:
            self.lista_de_canais.append(canal)

class ControleRemoto:
    # A MÁGICA ACONTECE AQUI!
    # O __init__ pede um parâmetro 'tv'. 
    # Isso significa que, para criar um controle, você PRECISA dizer qual TV ele controla.
    def __init__(self, tv):
        
        self.tv = tv
    
    def aumentaVolume(self):
        # O controle não tem volume próprio.
        # Ele acessa a TV guardada (self.tv) e manda ELA aumentar o volume.
        self.tv.aumentaVolume(90)
    
    def diminuiVolume(self):
        self.tv.diminuiVolume(90)
    
    def trocaCanal(self, canal):
        # Delegação: O controle recebe o comando, mas quem executa é a TV.
        self.tv.trocaCanal(canal)
        
    def sintonizaCanal(self, canal):
        self.tv.sintonizaCanal(canal)
    