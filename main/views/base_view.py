from abc import ABC, abstractmethod

import PySimpleGUI as sg


class BaseView(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @staticmethod
    def button(name, key, size=10):
        return sg.Button(name, key=key, size=(size, 1), font=('Helvetica', 15))

    @staticmethod
    def form_field(label, key, required=True, password=False, size=(30, 2), text_size=(8, 1)):
        return [
            sg.Text(label, font=('Helvetica', 15), text_color='black', size=text_size),
            sg.Text('*', font=('Helvetica', 15), text_color='red' if required else sg.theme_background_color()),
            sg.InputText('', size=size, font=('Helvetica', 20), key=key, password_char='*' if password else '')
        ]

    @staticmethod
    def display_msg(msg: str, success):
        sg.Popup('Sucesso' if success else 'Erro',
                 msg, font=('Helvetica', 15),
                 background_color='green' if success else 'red')
