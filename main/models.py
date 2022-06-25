from django.db import models


def is_valid_user_type(value):
    return value in ['admin', 'teacher', 'player']


class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12, null=True)
    password = models.CharField(max_length=256)
    balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    type = models.CharField(max_length=7, validators=[is_valid_user_type])

    @staticmethod
    def generate_hashed_password(plain_text_password):
        return bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())

    def authenticate(self, password):
        return bcrypt.checkpw(password, self.password)

    def __str__(self):
        return f'{self.id} | {self.first_name} {self.last_name}'


class Court(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.id} | {self.name}'


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


class ArenaInformation(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    hour_value = models.PositiveSmallIntegerField()
    opening_hour = models.PositiveSmallIntegerField()
    closing_hour = models.PositiveSmallIntegerField()

# from main.models import *
# from datetime import datetime, date, time
# p = User.objects.last()
# c = Court.objects.last()
# day = date(2022, 6, 26)
# start_time = 19
# end_time = 21
# Reservation.objects.create(reserved_by=p, court=c, day=day, start_time=start_time, end_time=end_time, hour_value=60)
