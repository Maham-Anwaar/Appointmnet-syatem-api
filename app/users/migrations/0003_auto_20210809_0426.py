# Generated by Django 3.2.6 on 2021-08-09 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_appointment_patient'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
