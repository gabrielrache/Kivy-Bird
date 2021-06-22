from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Incrementador(BoxLayout):
    pass

class BodyEvo(App):
    def build(self):
        return Incrementador()

BodyEvo().run()