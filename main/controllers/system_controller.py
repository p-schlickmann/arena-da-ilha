from main.controllers.auth_controller import AuthController


class SystemController:
    def __init__(self):
        self.__auth_controller = AuthController(self)

    def start_system(self):
        self.open_initial_view()

    def exit(self):
        return exit(0)

    def user_is_logged_in(self):
        return False

    def open_initial_view(self):
        if self.user_is_logged_in():
            pass
        else:
            self.__auth_controller.open_view()
