# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 13:24:22 2019

@author: carol
"""
import matplotlib.pyplot as plt
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        list = [80,60,70,65,63,60,95,179,100,100,100,100,185,120,110,100,100,
                179,130,120,110,100,95,90,85]
        output =""
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 1
#        for num in list:
#            if num <60:
#                print("Your bloodsugar list is dangerously low get to a hospital immediately")
#            if num>59 and num<90:
#                print("Your bloodsugar is low but normal")
#            if num>89 and num<120:
#                print("Your bloodsugar is normal")
#            if num>119 and num<180:
#                print("Your bloodsugar is high")
#            if num>179:
#                print ("Your bloodsugar is too high get to a hospital immediately")

        self.inside.add_widget(Label(text=output))
        self.inside.add_widget(plt.show())
        
        




        self.add_widget(self.inside)

#        self.submit = Button(text="Submit", font_size=40)
#        self.submit.bind(on_press=self.pressed)
#        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.name.text
        last = self.lastName.text
        email = self.email.text

        print("Name:", name, "Last Name:", last, "Email:", email)
        self.name.text = ""
        self.lastName.text = ""
        self.email.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()