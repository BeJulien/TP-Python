# coding: utf-8

from .app import MainApp

__author__ = "Julien Benac"


def create_app() -> MainApp:
    return MainApp()
