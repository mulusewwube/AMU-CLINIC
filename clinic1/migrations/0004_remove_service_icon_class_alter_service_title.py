# Generated by Django 4.2.7 on 2023-12-26 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic1', '0003_service_delete_apointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='icon_class',
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
