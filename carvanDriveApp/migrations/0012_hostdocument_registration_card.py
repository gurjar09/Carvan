# Generated by Django 5.0.3 on 2024-04-08 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carvanDriveApp', '0011_hostdetails_hostdocument_delete_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostdocument',
            name='registration_card',
            field=models.FileField(default=0, upload_to='images'),
            preserve_default=False,
        ),
    ]