# Generated by Django 5.0.3 on 2024-04-11 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carvanDriveApp', '0026_remove_hostdocument_car_insurence_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostdocument',
            name='adhar_card',
            field=models.ImageField(upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='hostdocument',
            name='car_insurance',
            field=models.ImageField(upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='hostdocument',
            name='driving_license',
            field=models.ImageField(upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='hostdocument',
            name='puc_card',
            field=models.ImageField(upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='hostdocument',
            name='registration_card',
            field=models.ImageField(upload_to='documents/'),
        ),
    ]
