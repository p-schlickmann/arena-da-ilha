import PySimpleGUI as sg
from main.views.base_view import BaseView


class AdminView(BaseView):

    def __init__(self):
        super().__init__()
        self.__window = None

    def open(self):
        window = sg.Window('Arena da Ilha - ADM', element_justification='c', size=(700, 450)).Layout([
            [sg.Text('Olá, ADM', font=('Open Sans', 20), text_color='black', )],
            [self.blue_button('Voltar', 1)],
        ])
        self.__window = window
        button, values = self.__window.Read()
        self.__window.Close()
        return button
