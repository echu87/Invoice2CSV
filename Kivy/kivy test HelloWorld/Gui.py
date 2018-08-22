from kivy.app import App
from kivy.uix.button import  Button
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

class HelloWorld(App):
    def build(self):
        btn = Button(text= "Push Me!")
        return btn

class World(App):
    def build(self):
        return HelloWorld()


if __name__ == '__main__':
    World().run()