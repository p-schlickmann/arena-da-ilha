# Generated by Django 3.2 on 2022-05-25 17:44

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=12, null=True)),
                ('password', models.CharField(max_length=256)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('type', models.CharField(max_length=7, validators=[main.models.is_valid_user_type])),
            ],
        ),
    ]
