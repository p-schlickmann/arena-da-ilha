from django.db import transaction
from django.db.models import Q

from main.models import Reservation, Court, ArenaInformation, User
from main.views.player_view import PlayerView


class PlayerController:

    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__view = PlayerView()

    def open_view(self):
        balance = self.__system_controller.get_current_user_balance()
        button, values = self.__view.open(Reservation.get_available_days_to_make_a_reservation(), balance)
        if button == 0:
            selected_option = values[0][0]
            if selected_option:
                self.select_reservation_time(selected_option)
        self.__system_controller.open_initial_view()

    def attempt_reservation(self, day, start_time, end_time, court, total_value, hour_value):
        already_made = Reservation.objects.select_related('court').filter(
            Q(start_time=start_time) | Q(end_time=end_time) | Q(end_time__gte=end_time, start_time__lte=start_time),
            day=day, court__name=court
        ).exists()
        if already_made:
            return False, 'Essa quadra já foi reservada nesse dia/hora.'
        user = User.objects.get(id=self.__system_controller.logged_in_user_id())
        if user.has_credits(total_value):
            with transaction.atomic():
                Reservation.objects.create(
                    start_time=start_time, end_time=end_time, day=day,
                    court_id=court, reserved_by=user, hour_value=hour_value
                )
                user.balance = user.balance - total_value
                user.save()
                return True, 'Reserva efetuada com sucesso.'
        else:
            return False, 'Você não tem créditos suficientes.'

    @staticmethod
    def validate_gap_between_times(start, end, time_list):
        """
        Selected times cannot have a gap, they must all be in a perfect sequence.
        Example: [11:00, 12:00, 13:00]
        Invalid example: [11:00, 12:00, 14:00]
        """
        gap = end - start
        return gap <= len(time_list)

    def handle_selected_times(self, time_list):
        start_time = min(time_list)
        end_time = max(time_list) + 1
        valid = self.validate_gap_between_times(start_time, end_time, time_list)
        if valid:
            time_formatted = f'{start_time}:00 - {end_time}:00'
        else:
            self.__view.display_msg(
                'Caso queira selecionar mais de um horário, selecione horários seguidos.',
                False
            )
            time_formatted = ''
        return start_time, end_time, time_formatted

    def select_reservation_time(self, selected_day):
        button, selected_values = self.__view.open_select_reservation_time(
            Reservation.get_available_time_to_make_a_reservation(selected_day), selected_day
        )
        if int(button) == 0:
            return
        if not selected_values:
            self.__view.display_msg('Selecione um horário!', False)
            return
        if button == 1:
            time_list = list(map(lambda time_string: int(time_string.split(':')[0]), selected_values))
            start_time, end_time, time_formatted = self.handle_selected_times(time_list)
            if not time_formatted:
                return
            available_courts = Court.get_available_courts(selected_day, start_time, end_time)
            if available_courts:
                hour_value = ArenaInformation.objects.first().hour_value
                total_value = (end_time - start_time) * hour_value
                button = self.__view.open_select_courts(selected_day, time_formatted, available_courts, total_value)
                if button[0] == 1:
                    selected_court = button[1][0]
                    if selected_court:
                        reservation_successful, msg = self.attempt_reservation(
                            selected_day, start_time, end_time,
                            selected_court[0], total_value, hour_value
                        )
                        self.__view.display_msg(msg, success=reservation_successful)
                    else:
                        self.__view.display_msg('Selecione uma quadra!', False)
            else:
                self.__view.display_msg('Não há quadras disponíveis no horário selecionado.', False)
