# coding: utf-8

from kivy.lang import Builder
from kivymd.app import MDApp

from os.path import dirname
from os.path import join

KV_MANAGER = join(dirname(__file__), "screen", "kv", "manager.kv")


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"

        return Builder.load_file(KV_MANAGER)
