import itertools
from datetime import timedelta, date

import bcrypt
from django.db import models
from django.db.models import Q


def is_valid_user_type(value):
    return value in ['admin', 'teacher', 'player']


class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12, null=True)
    password = models.CharField(max_length=256)
    balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    user_type = models.CharField(max_length=7, validators=[is_valid_user_type])

    @staticmethod
    def generate_hashed_password(plain_text_password):
        return bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())

    def authenticate(self, password):
        return bcrypt.checkpw(password, self.password)

    def has_credits(self, amount):
        return float(self.balance) >= float(amount)

    def __str__(self):
        return f'{self.id} | {self.first_name} {self.last_name}'


class Court(models.Model):
    name = models.CharField(max_length=64, primary_key=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_available_courts(day, start, end):
        available_courts = Court.objects.values_list('name')
        unavailable_courts = Reservation.objects.select_related('court').filter(
            Q(start_time=start) | Q(end_time=end) | Q(end_time__gte=end, start_time__lte=start), day=day,
        ).values_list('court__name')
        return list(map(lambda x: x[0], available_courts.difference(unavailable_courts)))


class Lesson(models.Model):
    pass


class Reservation(models.Model):
    reserved_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_reservations')
    court = models.ForeignKey(Court, on_delete=models.PROTECT, related_name='court_reservations')
    lesson = models.OneToOneField(Lesson, on_delete=models.PROTECT, related_name='reservation', null=True)
    day = models.DateField()
    start_time = models.PositiveSmallIntegerField()
    end_time = models.PositiveSmallIntegerField()
    hour_value = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.id} | {self.day} {self.start_time}-{self.end_time} | {self.court.name}'

    @staticmethod
    def get_available_days():
        today = date.today()
        court_amount = Court.objects.count()
        reservations = Reservation.objects.filter(
            day__range=(today, today + timedelta(days=7))
        ).values('day', 'end_time', 'start_time')
        grouped_by_day = itertools.groupby(reservations, lambda d: d.get('day').strftime('%Y-%m-%d'))
        amount_of_hours_already_reserved_per_day = [
            (
                day,
                sum(
                    [key['end_time'] - key['start_time'] for key in this_day]
                )
            )
            for day, this_day in grouped_by_day
        ]
        available_days = {(today + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7)}
        full_booked_days = set(
            filter(
                lambda x: bool(x),
                (
                    map(
                        lambda x: x[0] if x[1] >= 14 * court_amount else '',
                        amount_of_hours_already_reserved_per_day
                    )
                )
            )
        )
        return sorted(list(available_days.difference(full_booked_days)))

    @staticmethod
    def get_available_times(day):
        print(day)
        courts_id = Court.objects.values_list('name', flat=True)
        opening, closing = ArenaInformation.get_opening_and_closing_hour()
        print(opening, closing)
        possible_times = [i for i in range(opening, closing)]
        available_times = set()
        for court_id in courts_id:
            for t in possible_times:
                available_times.add(f'{t}-{court_id}')
        booked_times_intervals = Reservation.objects.filter(
            day=day
        ).values_list('start_time', 'end_time', 'court__name')
        booked_time_list = [[f'{i}-{court_id}' for i in range(start, end)] for start, end, court_id in
                            booked_times_intervals]
        booked_times = []
        for t in booked_time_list:
            booked_times.extend(t)
        av = list(map(lambda x: f'{x}:00', sorted(
            set([int(hour.split('-')[0]) for hour in set(available_times).difference(set(booked_times))]))))
        return av


class ArenaInformation(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    hour_value = models.PositiveSmallIntegerField()
    opening_hour = models.PositiveSmallIntegerField()
    closing_hour = models.PositiveSmallIntegerField()

    @staticmethod
    def get_opening_and_closing_hour():
        info = ArenaInformation.objects.first()
        return info.opening_hour, info.closing_hour

    @staticmethod
    def get_hour_value():
        return ArenaInformation.objects.first().hour_value

# from main.models import *
# from datetime import datetime, date, time
# p = User.objects.last()
# c = Court.objects.last()
# day = date(2022, 6, 26)
# start_time = 19
# end_time = 21
# Reservation.objects.create(reserved_by=p, court=c, day=day, start_time=start_time, end_time=end_time, hour_value=60)
