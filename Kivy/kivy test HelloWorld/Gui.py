from kivy.app import App
from kivy.uix.button import  Button
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class ScatterTextWidget(BoxLayout):
    pass
class hello_world(App):
    def build(self):
        btn = Button(text= "Push Me!")
        def callback(instance):
            print("Hellon't")
        btn.bind(on_press=callback)
        return ScatterTextWidget()





if __name__ == '__main__':
    hello_world().run()