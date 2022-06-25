import itertools
from datetime import timedelta, date

from main.models import Reservation
from main.views.player_view import PlayerView


class PlayerController:

    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__view = PlayerView()

    def get_available_days_to_make_a_reservation(self):
        qs = Reservation.objects.filter(
            day__range=(date.today(), date.today() + timedelta(days=7))).values('day', 'end_time', 'start_time')
        grouped = itertools.groupby(qs, lambda d: d.get('day').strftime('%Y-%m-%d'))
        hours_per_day = [
            (day, sum([key['end_time'] - key['start_time'] for key in this_day]))
            for day, this_day in grouped
        ]

    def get_available_time_to_make_a_reservation(self):
        return ['19:00', '20:00', '23:00']

    def get_available_courts(self, day, start_time, end_time):
        return ['Quadra 1', 'Quadra 2']

    def open_view(self):
        button, values = self.__view.open(self.get_available_days_to_make_a_reservation())
        if button == 0:
            selected_option = values[0][0]
            if selected_option:
                self.select_reservation_time(selected_option)
        self.__system_controller.open_initial_view()

    def attempt_reservation(self, day, start_time, end_time, court):
        return True, 'Reserva bem sucedida'

    @staticmethod
    def validate_gap_between_times(start, end, time_list):
        """
        Selected times cannot have a gap, they must all be in a perfect sequence.
        Example: [11:00, 12:00, 13:00]
        Invalid example: [11:00, 12:00, 14:00]
        """
        gap = int(end.split(':')[0]) - int(start.split(':')[0])
        return gap <= len(time_list)

    def handle_selected_times(self, time_list):
        start_time = min(time_list)
        end_time = max(time_list)
        if start_time != end_time:
            valid = self.validate_gap_between_times(start_time, end_time, time_list)
            if valid:
                time_formatted = f'{start_time} - {end_time}'
            else:
                self.__view.display_msg(
                    'Caso queira selecionar mais de um horário, selecione horários seguidos.',
                    False
                )
                time_formatted = ''
        else:
            time_formatted = start_time
        return start_time, end_time, time_formatted

    def select_reservation_time(self, selected_day):
        button, selected_values = self.__view.open_select_reservation_time(
            self.get_available_time_to_make_a_reservation(), selected_day
        )
        if not selected_values:
            self.__view.display_msg('Selecione um horário!', False)
            return
        if button == 1:
            start_time, end_time, time_formatted = self.handle_selected_times(selected_values)
            if not time_formatted:
                return
            available_courts = self.get_available_courts(selected_day, start_time, end_time)
            if available_courts:
                button = self.__view.open_select_courts(selected_day, time_formatted, available_courts)
                if button[0] == 1:
                    selected_court = button[1][0]
                    if selected_court:
                        reservation_successful, msg = self.attempt_reservation(
                            selected_day, start_time,
                            end_time, selected_court
                        )
                        self.__view.display_msg(msg, success=reservation_successful)
                    else:
                        self.__view.display_msg('Selecione uma quadra!', False)
            else:
                self.__view.display_msg('Não há quadras disponíveis no horário selecionado.', False)
