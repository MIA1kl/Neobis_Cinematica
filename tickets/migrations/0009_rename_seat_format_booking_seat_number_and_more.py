# Generated by Django 4.2.1 on 2023-05-22 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_remove_seatformat_price'),
        ('tickets', '0008_booking_room_format_booking_seat_format_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='seat_format',
            new_name='seat_number',
        ),
        migrations.AddField(
            model_name='feedback',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='movies.movie'),
        ),
    ]
