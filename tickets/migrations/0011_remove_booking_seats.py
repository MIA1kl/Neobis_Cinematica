# Generated by Django 4.2.1 on 2023-05-22 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0010_remove_ticket_seat_remove_ticket_showtime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='seats',
        ),
    ]