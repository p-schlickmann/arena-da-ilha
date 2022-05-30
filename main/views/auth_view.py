import PySimpleGUI as sg

from main.views.base_view import BaseView


class AuthView(BaseView):
    def __init__(self):
        super().__init__()
        self.__window = None

    def open(self):
        buttons = [
            [self.button('Entrar', 2)],
            [self.button('Registrar', 1)],
        ]
        div = [
            [sg.Text('Entrar ou Registrar', font=('Helvetica', 15), text_color='black', )],
            [sg.Column(buttons, pad=(0, 25))],
        ]
        window = sg.Window('Arena da Ilha - Selecionar', element_justification='c', size=(700, 450)).Layout([
            [sg.Column(div, pad=(0, 50), element_justification='c')]
        ])
        self.__window = window
        button, values = self.__window.Read()
        self.__window.Close()
        return button

    def display_invalid_credentials(self):
        self.display_msg('Invalid Authentication Credentials', False)

    def display_register(self):
        inputs = [
            self.form_field('Nome', 'first_name'),
            self.form_field('Sobrenome', 'last_name'),
            self.form_field('Email', 'email'),
            self.form_field('Telefone', 'phone_number', required=False),
            self.form_field('Senha', 'plain_password', password=True),
            [
                sg.Text('Sou um', font=('Helvetica', 15), text_color='black', size=(8, 1)),
                sg.Text('*', font=('Helvetica', 15), text_color='red'),
                sg.Radio('Professor', "RADIO1", default=False, key='is_teacher', font=('Helvetica', 15)),
                sg.Radio('Jogador', "RADIO1", default=False, key='is_player', font=('Helvetica', 15))
            ],
        ]
        div = [
            [sg.Text('Registrar-se', font=('Helvetica', 15), text_color='black', )],
            [sg.Column(inputs, pad=(0, 50))],
            [self.button('Voltar', 3), self.button('Cadastrar', 2)]
        ]
        window = sg.Window('Arena da Ilha - Registrar', element_justification='c', size=(700, 450)).Layout([
            [sg.Column(div, pad=(0, 25), element_justification='c')]
        ])
        self.__window = window
        button, values = self.__window.Read()
        self.__window.Close()
        return button, values

    def display_login(self):
        inputs = [
            self.form_field('Email', 'email'),
            self.form_field('Senha', 'password', password=True),
        ]
        div = [
            [sg.Text('Entrar', font=('Helvetica', 15), text_color='black', )],
            [sg.Column(inputs, pad=(0, 50))],
            [self.button('Voltar', 1), self.button('Entrar', 2)],
        ]

        window = sg.Window('Arena da Ilha - Entrar', element_justification='c', size=(700, 450)).Layout([
            [sg.Column(div, pad=(0, 50), element_justification='c')]
        ])

        self.__window = window
        button, values = self.__window.Read()
        self.__window.Close()
        return button, values
