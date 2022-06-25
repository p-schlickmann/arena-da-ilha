from main.controllers.admin_controller import AdminController
from main.controllers.auth_controller import AuthController
from main.controllers.player_controller import PlayerController
from main.controllers.teacher_controller import TeacherController
from main.models import User


class SystemController:
    def __init__(self):
        self.__auth_controller = AuthController(self)
        self.__teacher_controller = TeacherController(self)
        self.__admin_controller = AdminController(self)
        self.__player_controller = PlayerController(self)
        self.__logged_in_user = None

    def start_system(self):
        self.open_initial_view()

    def exit(self):
        return exit(0)

    def set_logged_in_user(self, user):
        self.__logged_in_user = user

    def logged_in_user_id(self):
        return self.__logged_in_user['id']

    def get_current_user_balance(self):
        return float(User.objects.get(id=self.logged_in_user_id()).balance)

    def open_initial_view(self):
        self.__logged_in_user = {
            'user_type': 'player',
            'id': '2'
        }
        if self.__logged_in_user is not None:
            print(self.__logged_in_user)
            controllers = {
                'admin': self.__admin_controller,
                'teacher': self.__teacher_controller,
                'player': self.__player_controller,
            }
            return controllers[self.__logged_in_user['user_type']].open_view()
        else:
            self.__auth_controller.open_view()
