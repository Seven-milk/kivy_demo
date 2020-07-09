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
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup


class MyGrid(Widget):
    base_time = ObjectProperty(None)

    def btn_cal(self):
        show_popup()

    def btn_modify(self):
        with open('start.text', 'w') as f:
            f.write(self.base_time.text)


class MyApp(App):
    def build(self):
        return MyGrid()


class P(FloatLayout):
    date = ObjectProperty(None)
    base_time = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(FloatLayout, self).__init__(**kwargs)
        self.date = self.cal()
        self.base_time = self.show()

    def cal(self):
        with open('start.text', 'r') as f:
            f_read = f.read().split()
            start = datetime.date(int(f_read[0]), int(f_read[1]), int(f_read[2]))

        time_delta = datetime.timedelta(days=28)
        now = datetime.date.today()
        dif = now - start
        return str(start + ((dif // time_delta) + 1) * time_delta)

    def show(self):
        with open('start.text', 'r') as f:
            f_read = f.read().split()
            return str(datetime.date(int(f_read[0]), int(f_read[1]), int(f_read[2])))


def show_popup():
    show = P()

    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None, None), size=(400, 400))

    popupWindow.open()


if __name__ == "__main__":
    MyApp().run()
