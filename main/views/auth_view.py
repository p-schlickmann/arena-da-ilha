import PySimpleGUI as sg

from main.views.base_view import BaseView


class AuthView(BaseView):
    def __init__(self):
        super().__init__()
        self.__window = None

    def open(self):
        window = sg.Window('Arena da Ilha - Selecionar', element_justification='c', size=(700, 450)).Layout([
            [sg.Text('Entrar ou Registrar', font=('Open Sans', 20), text_color='black',)],
            [self.blue_button('Entrar', 2)],
            [self.blue_button('Registrar', 1)],
        ])
        self.__window = window
        button, values = self.__window.Read()
        self.__window.Close()
        return button

    def display_register(self):
        pass
