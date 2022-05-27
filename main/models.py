import bcrypt
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
        return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

    def __str__(self):
        return f'{self.id} | {self.first_name} {self.last_name}'


class Lesson(models.Model):
    id = models.BigAutoField(primary_key=True)
    price = models.CharField(max_length=64)
    min_players = models.CharField(4)
    max_players = models.CharField(4)

    def __str__(self):
        return f'{self.id} | {self.price} | {self.min_players} | {self.max_players}'