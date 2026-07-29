from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MeuAppAndroid(App):
    def build(self):
        self.contador = 0
        
        # Layout vertical com margens
        layout = BoxLayout(
            orientation='vertical',
            padding=30,
            spacing=20
        )
        
        # Rótulo de exibição
        self.label = Label(
            text="📱 Meu App no Android",
            font_size='28sp',
            bold=True
        )
        
        # Botão interativo
        self.btn = Button(
            text="Clicar (+1)",
            font_size='22sp',
            size_hint=(1, 0.4),
            background_color=(0.1, 0.5, 0.9, 1)
        )
        
        # Vincular o clique do botão à função
        self.btn.bind(on_press=self.incrementar)
        
        # Adicionar os elementos na tela
        layout.add_widget(self.label)
        layout.add_widget(self.btn)
        
        return layout

    def incrementar(self, instance):
        self.contador += 1
        self.label.text = f"Cliques: {self.contador}"

if __name__ == '__main__':
    MeuAppAndroid().run()

