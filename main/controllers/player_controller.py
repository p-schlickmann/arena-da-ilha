from main.views.player_view import PlayerView


class PlayerController:

    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__view = PlayerView()

    def open_view(self):
        options = {
        }
        selected_option = self.__view.open()
        options[selected_option]()
