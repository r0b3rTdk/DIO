from kivy.app import App
from kivy.uix.label import Label

# 1. HERANÇA (POO)
# Sua classe MainApp "é um" App. Ela ganha todos os poderes de um aplicativo Kivy.
class MainApp(App):
    
    # 2. INSTANCIAÇÃO COM PARÂMETROS
    # Aqui criamos o objeto Label, mas passamos configurações extras:
    def build(self):
        label = Label(text='30 no comando',
                    # 3. SIZE_HINT (Dica de Tamanho)
                    # No Kivy, evitamos usar pixels fixos (ex: 200px) porque celulares têm tamanhos diferentes.
                    # Usamos porcentagem de 0 a 1.
                    # (.5, .5) significa: "Ocupe 50% da largura e 50% da altura da tela".
                    size_hint=(.5, .5),
                    # 4. POS_HINT (Dica de Posição)
                    # É um dicionário {} que define onde o widget vai ficar ancorado.
                    # 'center_x': .5 -> O centro do texto fica em 50% da largura da tela (no meio horizontal).
                    # 'center_y': .5 -> O centro do texto fica em 50% da altura da tela (no meio vertical).
                    pos_hint={'center_x': .5, 'center_y': .5})
        return label

# Só roda o app se esse arquivo for executado diretamente
if __name__ == '__main__':
    app = MainApp()
    app.run()