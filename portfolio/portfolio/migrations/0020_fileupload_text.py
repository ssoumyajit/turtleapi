# Generated by Django 2.2.6 on 2020-08-11 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_auto_20200807_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='text',
            field=models.CharField(default='', max_length=255),
        ),
    ]
