# Generated by Django 4.2.1 on 2023-05-21 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_seatformat_room_room_format_seat_seat_format'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seat',
            old_name='seat_format',
            new_name='seat_number',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='number',
        ),
    ]