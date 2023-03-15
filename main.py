import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

class ClickerApp(App):
    count = 0

    def build(self):
        self.label = Label(text="0")
        self.button = Button(text="Click me!")
        self.button.bind(on_press=self.on_button_click)
        return self.label, self.button

    def on_button_click(self, instance):
        self.count += 1
        self.label.text = str(self.count)

if __name__ == '__main__':
    ClickerApp().run()
