# Generated by Django 5.0.3 on 2024-04-05 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carvanDriveApp', '0005_alter_hostdocument_car_insurence_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostdocument',
            name='car_insurence',
            field=models.FileField(upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='hostdocument',
            name='driving_licence',
            field=models.FileField(upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='hostdocument',
            name='identity',
            field=models.FileField(upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='hostdocument',
            name='puc',
            field=models.FileField(upload_to='pics'),
        ),
    ]
