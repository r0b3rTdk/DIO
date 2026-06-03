import math # Importando a biblioteca para usar o valor exato de PI

class Esfera:
    # 1. O CONSTRUTOR (__init__)
    # Este método roda AUTOMATICAMENTE assim que você cria a bola.
    # Ele serve para definir o "estado inicial" do objeto.
    # self: sou eu (a bola sendo criada).
    # cor, raio: são os dados que chegam de fora.
    def __init__(self,cor,raio):
        self.cor = cor
        self.raio = raio
        
    def volume(self):
        # Aqui usamos 'self.raio' para pegar o raio ESPECÍFICO desta bola.
        # Se usássemos apenas 'raio', o Python procuraria uma variável local e daria erro.
        vol = (4/3)*math.pi*(self.raio**3)
        return vol
    
    def area(self):
        ar = 4*math.pi*(self.raio**2)
        return ar

# 2. CRIANDO OBJETOS DISTINTOS
# Ao chamar Esfera(...), o Python vai direto no __init__
bola1 = Esfera('vermelha', 4) # O self vira a bola1, cor vira 'vermelha', raio vira 4
bola2 = Esfera('azul', 7) # O self vira a bola2, cor vira 'azul', raio vira 7


print(f'O volume da bola 1 e {bola1.volume()}cm^3')
print(f'A area superficial da bola 1 e {bola1.area()}cm^2')

# --- A PARTE CURIOSA (O PULO DO GATO) ---

# Jeito Clássico (Açúcar Sintático):
# Você diz: "Objeto bola1, calcule seu volume".
# O Python traduz isso automaticamente para: Classe.metodo(objeto)
print(bola1.volume())

# Jeito "Manual" (O que o Python faz nos bastidores):
# Você diz: "Classe Esfera, use o método volume e aplique na bola1".
# Aqui, você é obrigado a passar o 'self' (bola1) manualmente.
print(Esfera.volume(bola1))