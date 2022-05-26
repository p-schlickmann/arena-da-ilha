from abc import ABC, abstractmethod

import PySimpleGUI as sg


class BaseView(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @staticmethod
    def blue_button(name, key):
        return sg.Button(name, key=key, size=(15, 1), font=('Helvetica', 15))

    @staticmethod
    def display_msg(msg: str, success):
        sg.Popup('Sucesso' if success else 'Erro', msg, font=('Helvetica', 15))
