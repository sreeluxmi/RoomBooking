# Generated by Django 4.0.3 on 2023-06-16 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_roombooking_check_room_booking'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='roombooking',
            name='check_room_booking',
        ),
    ]