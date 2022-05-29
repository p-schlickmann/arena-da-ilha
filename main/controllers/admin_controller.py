from main.views.admin_view import AdminView


class AdminController:

    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__view = AdminView()

    def open_view(self):
        options = {
            1: self.register_court,
        }
        selected_option = self.__view.open()
        options[selected_option]()

    def register_court(self):
        pass