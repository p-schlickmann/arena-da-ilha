import logging
import django
from django.conf import settings

import django_settings
from main.controllers.system_controller import SystemController


settings.configure(default_settings=django_settings, DEBUG=True)
django.setup()


if __name__ == '__main__':
    while True:
        try:
            SystemController().start_system()
        except Exception as error:
            logging.exception(str(error))
            print('[!] Tivemos um problema inesperado no sistema!')
