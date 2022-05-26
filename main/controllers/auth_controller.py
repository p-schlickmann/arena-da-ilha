from main.models import User
from main.views.auth_view import AuthView


class AuthController:
    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__view = AuthView()

    def open_view(self):
        options = {
            1: self.register,
            2: self.login,
        }
        selected_option = self.__view.open()
        options[selected_option]()

    def register(self):
        user_info = self.__view.display_register()
        try:
            plain_password = user_info.pop('plain_password')
            hashed_password = User.generate_hashed_password(plain_password)
            User.objects.create(**user_info, password=hashed_password)
        except Exception as error:
            print(error)
            self.__view.display_msg('Tivemos um problema ao cadastrar seu usuário. Tente novamente mais tarde', False)
        else:
            self.__view.display_msg('Registrado com sucesso!', True)

    def login(self):
        pass
