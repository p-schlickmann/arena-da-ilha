import os
from time import sleep

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_settings')
django.setup()


from main.controllers.system_controller import SystemController


if __name__ == '__main__':
    while True:
        try:
            SystemController().start_system()
        except Exception as error:
            print('[!] Tivemos um problema inesperado no sistema! -> ', error)
            sleep(1)
