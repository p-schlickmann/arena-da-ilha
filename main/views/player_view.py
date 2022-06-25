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

    def open_select_reservation_time(self, available_time, selected_day):
        listbox = sg.Listbox(values=available_time, size=(30, 6), font=('Helvetica', 15),
                             select_mode='multiple')
        div = [
            [sg.Text('Olá, Jogador', font=('Helvetica', 15), text_color='black', )],
            [sg.Text(f'Nova reserva para o dia {selected_day}', font=('Helvetica', 15), text_color='black', )],
            [listbox],
            [self.button('Cancelar', 0), self.button('Próximo', 1)]
        ]
        window = sg.Window('Arena da Ilha - Jogador', element_justification='c', size=(700, 450)).Layout([
            [sg.Column(div, pad=(0, 50), element_justification='c')]
        ])
        self.__window = window
        button, values = self.__window.Read()
        selected_values = listbox.get()
        self.__window.Close()
        return button, selected_values

    def open_select_courts(self, selected_day, selected_time, courts):
        div = [
            [sg.Text('Olá, Jogador', font=('Helvetica', 15), text_color='black', )],
            [sg.Text(f'Nova reserva para o dia {selected_day} {selected_time}', font=('Helvetica', 15),
                     text_color='black', )],
            [sg.Listbox(values=courts, size=(30, 6), font=('Helvetica', 15))],
            [self.button('Cancelar', 0), self.button('Confirmar Reserva', 1, size=15)]
        ]
        window = sg.Window('Arena da Ilha - Jogador', element_justification='c', size=(700, 450)).Layout([
            [sg.Column(div, pad=(0, 50), element_justification='c')]
        ])
        self.__window = window
        button, values = self.__window.Read()
        self.__window.Close()
        return button, values
