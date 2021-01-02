# Generated by Django 2.2.6 on 2020-12-28 01:55

import artist.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artist', '0008_auto_20201228_0029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ev_event', models.CharField(default=None, max_length=20)),
                ('ev_photo', models.ImageField(default=None, upload_to='events_attended/')),
                ('ev_date', models.DateField(blank=True, default=None)),
                ('ev_content', models.TextField(blank=True, default=None)),
                ('ev_link', models.URLField(blank=True, default=None)),
                ('ev_artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Highlights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w_context', models.CharField(default=None, max_length=255)),
                ('w_photo', models.ImageField(default=None, upload_to='work/')),
                ('w_date', models.DateField(blank=True, default=None)),
                ('w_content', models.TextField(blank=True, default=None)),
                ('w_link', models.URLField(blank=True, default=None)),
                ('w_artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JudgingWorkshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jw_event', models.CharField(default=None, max_length=30)),
                ('jw_photo', models.ImageField(default=None, upload_to='judgingworkshop/')),
                ('jw_date', models.DateField(blank=True, default=None)),
                ('jw_content', models.TextField(blank=True, default=None)),
                ('jw_link', models.URLField(blank=True, default=None)),
                ('jw_artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='artist',
            name='artist_image',
            field=models.ImageField(blank=True, default=None, upload_to='covers/'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='artist_name',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='artist',
            name='country',
            field=django_countries.fields.CountryField(blank=True, default=None, max_length=2),
        ),
        migrations.AlterField(
            model_name='artist',
            name='crew',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='artist',
            name='fb',
            field=models.URLField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='artist',
            name='ig',
            field=models.URLField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='artist',
            name='introduction',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='artist',
            name='personal',
            field=models.URLField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='artist',
            name='quote',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='artist',
            name='style',
            field=models.CharField(blank=True, default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='g_upload_photo',
            field=models.ImageField(default=None, upload_to=artist.models.Gallery.scramble_uploaded_filename),
        ),
        migrations.DeleteModel(
            name='Work',
        ),
    ]