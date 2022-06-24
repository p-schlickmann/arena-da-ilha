import PySimpleGUI as sg

from main.views.base_view import BaseView


class PlayerView(BaseView):

    def __init__(self):
        super().__init__()
        self.__window = None

    def open(self, available_days):
        # buttons = [
        #     [self.button('Reservar quadra', 2, size=15)],
        # ]
        div = [
            [sg.Text('Olá, Jogador', font=('Helvetica', 15), text_color='black', )],
            [sg.Listbox(values=available_days, size=(30, 6), font=('Helvetica', 15),
                        bind_return_key=True, enable_events=True)],
        ]
        window = sg.Window('Arena da Ilha - Jogador', element_justification='c', size=(700, 450)).Layout([
            [sg.Column(div, pad=(0, 50), element_justification='c')]
        ])
        self.__window = window
        button, values = self.__window.Read()
        self.__window.Close()
        return button, values

    def open_select_reservation_time(self, available_time):
        div = [
            [sg.Text('Olá, Jogador', font=('Helvetica', 15), text_color='black', )],
            [sg.Listbox(values=available_time, size=(30, 6), font=('Helvetica', 15),
                        bind_return_key=True, enable_events=True)],
        ]
        window = sg.Window('Arena da Ilha - Jogador', element_justification='c', size=(700, 450)).Layout([
            [sg.Column(div, pad=(0, 50), element_justification='c')]
        ])
        self.__window = window
        button, values = self.__window.Read()
        self.__window.Close()
        return button, values