# Generated by Django 4.2.1 on 2023-05-21 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_remove_ticket_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='payment_method',
        ),
    ]
