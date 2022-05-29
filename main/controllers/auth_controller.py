from django.db import IntegrityError

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
        button, user_info = self.__view.display_register()
        is_teacher = user_info.pop('is_teacher')
        user_info.pop('is_player')
        if button == 3:
            return self.__system_controller.open_initial_view()
        try:
            plain_password = user_info.pop('plain_password')
            hashed_password = User.generate_hashed_password(plain_password)
            User.objects.create(
                **user_info, password=hashed_password,
                type='player' if not is_teacher else 'teacher'
            )
        except IntegrityError:
            self.__view.display_msg('Um usuário com esse endereço de email ja existe.', False)
        except Exception as error:
            print(error)
            self.__view.display_msg('Tivemos um problema ao tentar registrar seu usuário. Tente novamente mais tarde',
                                    False)
        else:
            self.__view.display_msg('Registrado com sucesso!', True)

    def login(self):
        button, values = self.__view.display_login()
        if button == 3:
            self.__system_controller.open_initial_view()
            return
        try:
            user = User.objects.get(email=values['email'])
        except User.DoesNotExist:
            self.__view.display_invalid_credentials()
        else:
            authenticated = user.authenticate(values['password'])
            if authenticated:
                self.__system_controller.set_logged_in_user({'user_type': user.type})
                self.__system_controller.open_initial_view()
            else:
                self.__view.display_invalid_credentials()
