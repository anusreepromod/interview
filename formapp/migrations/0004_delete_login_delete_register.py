# Generated by Django 4.0.2 on 2022-02-14 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='login',
        ),
        migrations.DeleteModel(
            name='register',
        ),
    ]
