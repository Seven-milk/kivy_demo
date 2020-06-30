# code: utf-8
# author: "Xudong Zheng" 
# email: Z786909151@163.com
import datetime
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text="how do you feel today", font_size=20))
        self.feel = TextInput(multiline=False)
        self.add_widget(self.feel)

        self.time = Button(text=u"Milk baby' special time", font_size=20)
        self.time.bind(on_press=self.lijia_date)
        self.add_widget(self.time)

    def lijia_date(self, instance):
        start = datetime.date(2020, 6, 12)
        time_delta = datetime.timedelta(days=28)
        now = datetime.date.today()
        dif = now - start
        date = start + ((dif // time_delta) + 1) * time_delta
        return date


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
