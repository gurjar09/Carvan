# Generated by Django 5.0.3 on 2024-04-08 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carvanDriveApp', '0012_hostdocument_registration_card'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hostdetails',
            old_name='car_number',
            new_name='mobile_number',
        ),
        migrations.RemoveField(
            model_name='hostdetails',
            name='img',
        ),
    ]
