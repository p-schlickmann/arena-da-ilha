from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_court'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('hour_value', models.PositiveSmallIntegerField()),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='court_reservations', to='main.court')),
                ('lesson', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='reservation', to='main.lesson')),
                ('reserved_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_reservations', to='main.user')),
            ],
        ),
    ]
