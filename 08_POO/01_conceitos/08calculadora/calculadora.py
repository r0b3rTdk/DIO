# --- SEÇÃO DE IMPORTAÇÕES ---
# Importa a classe base 'App' que todo aplicativo Kivy precisa herdar
from kivy.app import App
# Importa o 'BoxLayout', que organiza os elementos em caixas (vertical ou horizontal)
from kivy.uix.boxlayout import BoxLayout
# Importa o widget de botão
from kivy.uix.button import Button
# Importa o campo de texto (que usaremos como visor da calculadora)
from kivy.uix.textinput import TextInput

# --- CLASSE PRINCIPAL ---
class MainApp(App):
    # O método build é obrigatório no Kivy. Ele constrói a interface e retorna o widget raiz.
    def build(self):
        # Lista para definir quais caracteres são operações matemáticas
        self.operators = ["/", "*", "+", "-"]
        
        # Variável de controle (Flag) para saber se o último clique foi um operador.
        # Isso evita erros como digitar "5 ++ 5"
        self.last_was_operator = None
        
        # Guarda qual foi exatamente o último botão clicado (para lógica futura)
        self.last_button = None
        
        # Cria o layout principal que vai segurar tudo.
        # orientation="vertical" empilha os itens um embaixo do outro (Visor em cima, botões embaixo)
        main_layout = BoxLayout(orientation="vertical")
        
        # --- CONFIGURAÇÃO DO VISOR ---
        self.solution = TextInput(
            multiline=False,  # Calculadora não tem múltiplas linhas
            readonly=True,    # Impede que o usuário digite letras pelo teclado do PC
            halign="right",   # Alinha os números à direita (padrão de calculadoras)
            font_size=55      # Fonte grande para facilitar a leitura
        )
        # Adiciona o visor ao layout principal
        main_layout.add_widget(self.solution)
        
        # --- CONFIGURAÇÃO DOS BOTÕES ---
        # Matriz (lista de listas) que desenha o teclado numérico
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        
        # Loop Externo: Passa por cada LINHA da matriz acima
        for row in buttons:
            # Para cada linha da matriz, cria uma "caixa" horizontal
            h_layout = BoxLayout()
            
            # Loop Interno: Passa por cada ITEM dentro da linha (ex: "7", depois "8"...)
            for label in row:
                # Cria o botão visual
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                # O PULO DO GATO: O 'bind' conecta o clique do mouse à função python.
                # Quando clicar, ele chama self.on_button_press
                button.bind(on_press=self.on_button_press)
                
                # Adiciona o botão nessa linha horizontal
                h_layout.add_widget(button)
            
            # Depois de encher a linha com botões, adiciona a linha inteira ao layout vertical principal
            main_layout.add_widget(h_layout)
        
        # --- BOTÃO DE IGUAL ---
        # Cria o botão de igual separadamente pois ele ocupa uma linha inteira no final
        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        # Conecta o botão de igual a uma função diferente: a que calcula o resultado
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)
        
        # Retorna a interface pronta para o Kivy desenhar na tela
        return main_layout
    
    # --- LÓGICA DOS BOTÕES (NÚMEROS E OPERADORES) ---
    def on_button_press(self, instance):
        # Pega o texto que já está no visor
        current = self.solution.text
        # Pega o texto do botão que foi clicado (instance é o botão)
        button_text = instance.text 
        
        # Se clicou em "C" (Clear), limpa o visor
        if button_text == "C":
            self.solution.text = ""
        else:
            # Verifica se está tentando colocar dois operadores seguidos (ex: "++")
            # Se já tem texto, o último foi operador E o atual é operador: não faz nada (return)
            if current and (self.last_was_operator and button_text in self.operators):
                return
            # Verifica se está tentando começar a conta com um operador (ex: "*5")
            elif current == "" and button_text in self.operators:
                return
            else:
                # Se passou nas verificações, junta o texto antigo com o novo botão clicado
                new_text = current + button_text
                self.solution.text = new_text
        
        # Atualiza as variáveis de controle para o próximo clique
        self.last_button = button_text
        # Define como True se o botão atual foi um operador (+, -, *, /)
        self.last_was_operator = self.last_button in self.operators

    # --- LÓGICA DO RESULTADO (=) ---
    def on_solution(self, instance):
        text = self.solution.text
        if text:
            try:
                # A mágica acontece aqui: eval() pega uma string ("2+2") e executa como conta matemática
                # Depois, str() converte o resultado (4) volta para texto para poder exibir no visor
                solution = str(eval(self.solution.text))
                self.solution.text = solution
            except Exception:
                # Se der erro (ex: dividir por zero), mostra "Erro"
                self.solution.text = "Erro"

# --- EXECUÇÃO DO APP ---
# Essa verificação garante que o app só rode se esse arquivo for executado diretamente
if __name__ == "__main__":
    MainApp().run()