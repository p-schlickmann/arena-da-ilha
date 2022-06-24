from main.views.player_view import PlayerView


class PlayerController:

    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__view = PlayerView()

    def get_available_days_to_make_a_reservation(self):
        return ['22/06', '23/06', '23/07']

    def get_available_time_to_make_a_reservation(self):
        return ['19:00', '20:00', '23:00']

    def open_view(self):
        options = {
            2: self.select_reservation_time,
            3: self.select_court,
        }
        button, values = self.__view.open(self.get_available_days_to_make_a_reservation())
        print(button, 'BUTTON')
        if button == 0:
            selected_option = values[0][0]
            print(selected_option)
            if selected_option:
                button = 2
        options[button]()

    def select_reservation_time(self):
        button, values = self.__view.open_select_reservation_time(
            self.get_available_time_to_make_a_reservation()
        )
        if button == 0:
            selected_option = values[0][0]
            print(selected_option)

    def select_court(self):
        pass
