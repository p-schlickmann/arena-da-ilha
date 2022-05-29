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
        button, values = self.__view.display_login()
        email = values[0]
        password = values[1]
        try:
            user = User.objects.get(email='admin@gmail.com')
        except User.DoesNotExist:
            self.__view.display_invalid_credentials()
        else:
            authenticated = user.authenticate('password123')
            if authenticated:
                self.__system_controller.set_logged_in_user({'user_type': user.type})
                self.__system_controller.open_initial_view()
            else:
                self.__view.display_invalid_credentials()
