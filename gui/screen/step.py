# coding: utf-8

from kivy.properties import StringProperty

from kivymd.uix.boxlayout import MDBoxLayout


class StepWidget(MDBoxLayout):
    image_source = StringProperty()
    name = StringProperty()
    distance = StringProperty()
