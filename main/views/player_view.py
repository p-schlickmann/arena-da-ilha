import PySimpleGUI as sg
from main.views.base_view import BaseView


class PlayerView(BaseView):

    def __init__(self):
        super().__init__()
        self.__window = None

    def open(self):
        window = sg.Window('Arena da Ilha - Jogador', element_justification='c', size=(700, 450)).Layout([
            [sg.Text('Olá, Jogador', font=('Open Sans', 20), text_color='black',)],
        ])
        self.__window = window
        button, values = self.__window.Read()
        self.__window.Close()
        return button
