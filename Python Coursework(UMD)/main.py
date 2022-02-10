import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window


class MyGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def button(self):
        print("Name:", self.name.text, "Email:", self.email.text)
        print(("button is pressed"))

        self.name.text = ""
        self.email.text = ""


class MyApp(App):

    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()