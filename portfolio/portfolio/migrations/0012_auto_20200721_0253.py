# Generated by Django 2.2.6 on 2020-07-21 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_auto_20200721_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='g_resized_photo_path',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='g_upload_photo',
            field=models.ImageField(default='', upload_to='gallery/1595300002/'),
        ),
    ]
