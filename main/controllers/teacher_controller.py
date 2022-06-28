from main.views.teacher_view import TeacherView


class TeacherController:

    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__view = TeacherView()

    @staticmethod
    def get_available_court_to_make_a_reservation():
        return ['Quadra 1', 'Quadra 2', 'Quadra 3']

    @staticmethod
    def get_available_time_to_make_a_reservation():
        return ['19:00', '20:00', '23:00']

    @staticmethod
    def get_available_days_to_make_a_reservation():
        return ['22/06', '23/06', '23/07']

    def open_view(self):
        options = {
            1: self.register_lesson,
            2: self.add_credits,
            3: self.see_billing,
        }
        selected_option = self.__view.open()
        options[selected_option]()

    def register_lesson(self):
        if len(self.get_available_court_to_make_a_reservation()) == 0:
            self.__view.display_msg('Não há quadras disponíveis', False)
        else:
            button, values, court = self.__view.display_register_lesson(
                self.get_available_days_to_make_a_reservation(),
                self.get_available_time_to_make_a_reservation(),
                self.get_available_court_to_make_a_reservation()
            )
            if button == 2:
                self.open_view()
            elif button == 3 and (values['price'] == '' or values['minPlayers'] == '' or values['maxPlayers'] == ''):
                self.__view.display_msg('Preencha todos os campos', False)
                return self.register_lesson()
            else:
                if values["maxPlayers"] < values["minPlayers"]:
                    self.__view.display_msg("O máximo de jogadores deve ser maior que o mínimo de jogadores!", False)
                    return self.register_lesson()
                self.__view.display_msg(f'Aula cadastrada com sucesso '
                                        f'\nQuadra: {court[2]}'
                                        f'\nPreço: {values["price"]}'
                                        f'\nMinimo Jogadores: {values["minPlayers"]}'
                                        f'\nMaximo Jogadores: {values["maxPlayers"]}',
                                        True)

    def add_credits(self):
        print('Add Credits')

    def see_billing(self):
        print('See Billing')
