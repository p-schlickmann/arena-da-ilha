# Generated by Django 3.2 on 2022-06-22 18:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0002_auto_20220528_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Court',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True)),
            ],
        ),
    ]
