# Generated by Django 2.2.6 on 2020-08-07 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_fileupload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fileupload',
            old_name='f_photo',
            new_name='file',
        ),
    ]
