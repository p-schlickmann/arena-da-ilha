# Generated by Django 3.2 on 2022-06-24 20:34
from datetime import datetime

from django.db import migrations


def create_arena_information(apps, schema_editor):
    arena_information = apps.get_model('main', 'ArenaInformation')
    arena_information.objects.create(
        name='Arena da Ilha', address='Rua da UFSC, 777', hour_value=60,
        opening_hour=datetime.strptime('09:00', '%H:%M'), closing_hour=datetime.strptime('23:00', '%H:%M')
    )


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0006_arenainformation'),
    ]

    operations = [
        migrations.RunPython(
            create_arena_information,
            reverse_code=lambda apps, schema_editor: print('reverting arena information data migration...'))
    ]
