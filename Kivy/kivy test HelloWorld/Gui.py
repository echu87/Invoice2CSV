from kivy.app import App
from kivy.uix.button import  Button


class HelloWorld(App):
    def build(self):
        btn = Button(text= "Push Me!")
        return btn

class World(App):
    def build(self):
        return HelloWorld()


if __name__ == '__main__':
    World().run()