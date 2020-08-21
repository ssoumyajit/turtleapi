# Generated by Django 2.2.6 on 2020-07-22 05:42

from django.db import migrations, models
import portfolio.urls


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_auto_20200721_0253'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='judging',
            options={'ordering': ['-j_date']},
        ),
        migrations.AlterModelOptions(
            name='milestone',
            options={'ordering': ['-m_date']},
        ),
        migrations.AlterModelOptions(
            name='thought',
            options={'ordering': ['-t_date']},
        ),
        migrations.AlterModelOptions(
            name='workshop',
            options={'ordering': ['-w_date']},
        ),
        migrations.AddField(
            model_name='gallery',
            name='g_resizedpath',
            field=models.ImageField(blank=True, default='', upload_to='gallery/resized/'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='g_resized_photo_path',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='g_upload_photo',
            field=models.ImageField(default='', upload_to=portfolio.urls.Gallery.scramble_uploaded_filename),
        ),
        migrations.AlterField(
            model_name='judging',
            name='j_event_photo',
            field=models.ImageField(default='', upload_to=portfolio.urls.Judging.scramble_uploaded_filename),
        ),
        migrations.AlterField(
            model_name='milestone',
            name='m_photo',
            field=models.ImageField(default='', upload_to=portfolio.urls.Milestone.scramble_uploaded_filename),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='artist_image',
            field=models.FileField(default='', upload_to=portfolio.urls.Portfolio.scramble_uploaded_filename),
        ),
        migrations.AlterField(
            model_name='thought',
            name='t_photo',
            field=models.ImageField(default='', upload_to=portfolio.urls.Thought.scramble_uploaded_filename),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='w_photo',
            field=models.ImageField(default='', upload_to=portfolio.urls.Workshop.scramble_uploaded_filename),
        ),
    ]
