# Generated by Django 2.2.6 on 2020-12-24 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
    ]