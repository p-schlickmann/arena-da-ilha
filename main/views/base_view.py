from abc import ABC, abstractmethod

import PySimpleGUI as sg


class BaseView(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @staticmethod
    def button(name, key):
        return sg.Button(name, key=key, size=(10, 1), font=('Helvetica', 15))

    @staticmethod
    def form_field(label, key, required=True, password=False):
        return [
            sg.Text(label, font=('Helvetica', 15), text_color='black', size=(8, 1)),
            sg.Text('*', font=('Helvetica', 15), text_color='red' if required else sg.theme_background_color()),
            sg.InputText('', size=(30, 2), font=('Helvetica', 20), key=key, password_char='*' if password else '')
        ]

    @staticmethod
    def display_msg(msg: str, success):
        sg.Popup('Sucesso' if success else 'Erro', msg, font=('Helvetica', 15), )
