from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color

class Dibujador(Widget):
    def __init__(self, **kwargs):
        super(Dibujador, self).__init__(**kwargs)
        self.line_width = 3  # Grosor de la tinta
        self.color = (1, 1, 1)  # Color de la tinta (blanco)

    def on_touch_down(self, touch):
        with self.canvas:
            Color(*self.color)
            touch.ud['dibujo'] = Line(points=(touch.x, touch.y), width=self.line_width)

    def on_touch_move(self, touch):
        touch.ud['dibujo'].points += [touch.x, touch.y]

class MiApp(App):
    def build(self):
        return Dibujador()

if __name__ == "__main__":
    MiApp().run()
