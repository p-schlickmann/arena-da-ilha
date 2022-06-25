from main.views.teacher_view import TeacherView


class TeacherController:

    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__view = TeacherView()

    def get_available_days_to_make_a_reservation(self):
        return ['22/06', '23/06', '23/07']

    def get_available_time_to_make_a_reservation(self):
        return ['19:00', '20:00', '23:00']

    def get_available_court_to_make_a_reservation(self):
        return ['Quadra 1', 'Quadra 2', 'Quadra 3']

    def open_view(self):
        options = {
            1: self.register_lesson,
            2: self.add_credits,
            3: self.see_billing,
        }
        selected_option = self.__view.open()
        options[selected_option]()

    def register_lesson(self):
        button, values, court = self.__view.display_register_lesson(self.get_available_days_to_make_a_reservation(),
                                                                    self.get_available_time_to_make_a_reservation(),
                                                                    self.get_available_court_to_make_a_reservation())
        print(f'Quadra: {court}')

    def add_credits(self):
        print('Add Credits')

    def see_billing(self):
        print('See Billing')
