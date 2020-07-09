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
    date = ObjectProperty(None)

    def btn_cal(self):
        with open('start.text', 'r') as f:
            f_read = f.read().split()
            start = datetime.date(int(f_read[0]), int(f_read[1]), int(f_read[2]))

        time_delta = datetime.timedelta(days=28)
        now = datetime.date.today()
        dif = now - start
        date = start + ((dif // time_delta) + 1) * time_delta
        print("下次例假是：{}".format(date))

    def btn_modify(self):
        with open('start.text', 'w') as f:
            f.write(self.base_time.text)

    def btn_show(self):
        with open('start.text', 'r') as f:
            f_read = f.read().split()
            base_time = datetime.date(int(f_read[0]), int(f_read[1]), int(f_read[2]))
            print(base_time)


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
