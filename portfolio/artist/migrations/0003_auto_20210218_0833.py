# Generated by Django 2.2.6 on 2021-02-18 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0002_auto_20210218_0815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='owner',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='artistdata',
            old_name='owner',
            new_name='username',
        ),
    ]
