# Generated by Django 2.2.6 on 2020-12-28 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0007_artist_crew'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='w_datetime',
            field=models.DateField(auto_now=True),
        ),
    ]