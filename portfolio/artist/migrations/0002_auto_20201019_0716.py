# Generated by Django 2.2.6 on 2020-10-19 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
