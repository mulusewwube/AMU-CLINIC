# Generated by Django 4.2.7 on 2023-12-22 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='apointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('doctor', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]