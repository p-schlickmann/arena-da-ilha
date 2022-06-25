import PySimpleGUI as sg

from main.views.base_view import BaseView


class TeacherView(BaseView):

    def __init__(self):
        super().__init__()
        self.__window = None

    def open(self):
        window = sg.Window('Arena da Ilha - Professor', element_justification='c', size=(700, 450)).Layout([
            [sg.Text('Olá, Professor', font=('Open Sans', 20), text_color='black', )],
            [self.button('Cadastrar aula', 1, size=15)],
            [self.button('Adicionar créditos', 2, size=15)],
            [self.button('Ver faturamento', 3, size=15)],
        ])
        self.__window = window
        button, values = self.__window.Read()
        self.__window.Close()
        return button

    def display_register_lesson(self, available_days, available_time, available_court):
        divInputs = [
            self.form_field('Email', 'email'),
            self.form_field('Email', 'email'),
            self.form_field('Email', 'email'),
        ]

        window = sg.Window('Arena da Ilha - Professor', element_justification='c', size=(700, 450)).Layout([
            [sg.Text('Cadastrar Aula', font=('Open Sans', 20), text_color='black', )],
            [sg.Listbox(values=available_days, size=(30, 6), key='LISTA-QUADRAS', font=('Helvetica', 15),
                        bind_return_key=True, enable_events=True),
             [sg.Column(divInputs, pad=(0, 50), element_justification='c')]],
            [self.button('Voltar', 3)],
        ])
        self.__window = window
        court = []
        while True:
            button, values = self.__window.read()
            if button == sg.WIN_CLOSED or button == 3:
                break
            if button == 'LISTA-QUADRAS':
                if len(court) == 0:
                    window.Element('LISTA-QUADRAS').update(values=available_time)
                elif len(court) == 1:
                    window.Element('LISTA-QUADRAS').update(values=available_court)
                court.append(values['LISTA-QUADRAS'][0])
        self.__window.Close()
        return button, values, court

    def display_add_credits(self):
        pass

    def display_see_billing(self):
        pass
