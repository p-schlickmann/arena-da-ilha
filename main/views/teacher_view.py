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
        div_inputs = [
            self.form_field('Preço', 'price', size=(10, 2), text_size=(14, 1)),
            self.form_field('Min. Jogadores', 'minPlayers', size=(10, 2), text_size=(14, 1)),
            self.form_field('Max. Jogadores', 'maxPlayers', size=(10, 2), text_size=(14, 1)),
        ]

        div_list = [
            [sg.Listbox(values=available_days, size=(15, 6), key='LISTA-QUADRAS', font=('Helvetica', 15),
                        bind_return_key=True, enable_events=True)],
            [self.button('Reset', 1)]
        ]

        window = sg.Window('Arena da Ilha - Professor', element_justification='c', size=(700, 450)).Layout([
            [sg.Text('Cadastrar Aula', font=('Open Sans', 20), text_color='black', )],
            [sg.Column(div_list, pad=(0, 50), element_justification='c'),
             sg.Column(div_inputs, pad=(0, 50), element_justification='c')],
            [self.button('Voltar', 2), self.button('Cadastrar', 3)],
        ])
        self.__window = window
        court = []
        while True:
            button, values = self.__window.read()
            if button == 1:
                court = []
                window.Element('LISTA-QUADRAS').update(values=available_days)
            elif button == sg.WIN_CLOSED or button == 2 or button == 3:
                break
            elif button == 'LISTA-QUADRAS':
                if len(court) == 0:
                    window.Element('LISTA-QUADRAS').update(values=available_time)
                elif len(court) == 1:
                    window.Element('LISTA-QUADRAS').update(values=available_court)
                if len(court) >= 3:
                    court.pop(2)
                else:
                    court.append(values['LISTA-QUADRAS'][0])
        self.__window.Close()
        return button, values, court

    def display_add_credits(self):
        pass

    def display_see_billing(self):
        pass
