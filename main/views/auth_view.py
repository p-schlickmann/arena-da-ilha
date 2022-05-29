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

    def display_invalid_credentials(self):
        self.display_msg('Invalid Authentication Credentials', False)

    def display_register(self):
        return {
            'plain_password': 'password123',
            'first_name': 'pedro',
            'last_name': 'mendes',
            'email': 'admin@gmail.com'
        }

    def display_login(self):
        inputs = [
            [sg.Text(' Email', font=('Helvetica', 15), text_color='black'),
             sg.Text('*', font=('Helvetica', 15), text_color='red'),
             sg.InputText("", size=(30, 2), font=('Helvetica', 20))],
            [sg.Text('Senha', font=('Helvetica', 15), text_color='black'),
             sg.Text('*', font=('Helvetica', 15), text_color='red'),
             sg.InputText("", size=(30, 2), font=('Helvetica', 20), password_char='*')],
        ]

        div = [
            [sg.Text('Entrar', font=('Helvetica', 15), text_color='black', )],
            [sg.Column(inputs, pad=(0, 50))],
            [self.blue_button('Voltar', 1), self.blue_button('Entrar', 2)],
        ]

        window = sg.Window('Arena da Ilha - Entrar', element_justification='c', size=(700, 450)).Layout([
            [sg.Column(div, pad=(0, 50), element_justification='c')]
        ])

        self.__window = window
        button, values = self.__window.Read()
        self.__window.Close()
        return button, values
