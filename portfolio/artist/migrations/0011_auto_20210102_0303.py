# Generated by Django 2.2.6 on 2021-01-02 03:03

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0010_auto_20201228_0210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='highlights',
            old_name='w_artist',
            new_name='h_artist',
        ),
        migrations.RemoveField(
            model_name='highlights',
            name='w_content',
        ),
        migrations.RemoveField(
            model_name='highlights',
            name='w_context',
        ),
        migrations.RemoveField(
            model_name='highlights',
            name='w_date',
        ),
        migrations.RemoveField(
            model_name='highlights',
            name='w_link',
        ),
        migrations.RemoveField(
            model_name='highlights',
            name='w_photo',
        ),
        migrations.AddField(
            model_name='highlights',
            name='h_content',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='highlights',
            name='h_context',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='highlights',
            name='h_date',
            field=models.DateField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='highlights',
            name='h_link',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='highlights',
            name='h_photo',
            field=models.ImageField(default='', upload_to='work/'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='artist_image',
            field=models.ImageField(blank=True, default='', upload_to='covers/'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='artist_name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='artist',
            name='country',
            field=django_countries.fields.CountryField(blank=True, default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='artist',
            name='crew',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='artist',
            name='fb',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='artist',
            name='ig',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='artist',
            name='introduction',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='artist',
            name='personal',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='artist',
            name='quote',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='artist',
            name='style',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='events',
            name='ev_content',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='events',
            name='ev_date',
            field=models.DateField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='events',
            name='ev_event',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='events',
            name='ev_link',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='events',
            name='ev_photo',
            field=models.ImageField(default='', upload_to='events_attended/'),
        ),
        migrations.AlterField(
            model_name='judgingworkshop',
            name='jw_content',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='judgingworkshop',
            name='jw_date',
            field=models.DateField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='judgingworkshop',
            name='jw_event',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='judgingworkshop',
            name='jw_link',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='judgingworkshop',
            name='jw_photo',
            field=models.ImageField(default='', upload_to='judgingworkshop/'),
        ),
    ]
