# Generated by Django 4.2.1 on 2023-05-21 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_seatformat_room_room_format_seat_seat_format'),
        ('tickets', '0007_remove_booking_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='room_format',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.roomformat'),
        ),
        migrations.AddField(
            model_name='booking',
            name='seat_format',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.seatformat'),
        ),
        migrations.AddField(
            model_name='booking',
            name='ticket_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.tickettype'),
        ),
    ]