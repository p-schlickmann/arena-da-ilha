import PySimpleGUI as sg

from main.views.base_view import BaseView


class TeacherView(BaseView):

    def __init__(self):
        super().__init__()
        self.__window = None

    def open(self):
        window = sg.Window('Arena da Ilha - Professor', element_justification='c', size=(700, 450)).Layout([
            [sg.Text('Olá, Professor', font=('Open Sans', 20), text_color='black', )],
            [self.button('Cadastrar aula', 1)],
            [self.button('Adicionar créditos', 2)],
            [self.button('Ver faturamento', 3)],
        ])
        self.__window = window
        button, values = self.__window.Read()
        self.__window.Close()
        return button

    def display_register_lesson(self):
        pass

    def display_add_credits(self):
        pass

    def display_see_billing(self):
        pass
