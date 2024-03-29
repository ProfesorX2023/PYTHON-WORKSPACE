import kivy
kivy.require('1.10.0')
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.floatlayout import FloatLayout
Builder.load_string('''
<Flotante>
    Button:
        font_size: 40
        text: 'Uno'
        size_hint: 0.1, 0.1
        pos_hint: {"x":0, "y":0}
        background_color: (255,0,197)
    Button:
        font_size: 40
        text: 'Dos'
        size_hint: 0.2, 0.2
        pos_hint: {"x":0.07, "y":0.07}
        background_color: (255,0,123)
    Button:
        font_size: 40
        text: 'Tres'
        size_hint: 0.3, 0.3
        pos_hint: {"x":0.18, "y":0.18}
        background_color: (255,0,0)
    Button:
        font_size: 40
        text: 'Cuatro'
        size_hint: 0.4, 0.4
        pos_hint: {"x":0.4, "y":0.35}
        background_color: (0,255,0)
    Button:
        font_size: 40
        text: 'Cinco'
        size_hint: 0.5, 0.5
        pos_hint: {"x":0.6, "y":0.6}
        background_color: (0,0,255)
''')


class Flotante(FloatLayout):
    pass


class DemoApp(App):
    def build(self):
        return Flotante()

if __name__ == "__main__":
    DemoApp().run()