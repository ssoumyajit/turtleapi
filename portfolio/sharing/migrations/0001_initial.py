# Generated by Django 2.2.6 on 2021-01-24 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sharing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_teacher_name', models.CharField(default='', max_length=255)),
                ('s_teacher_country', django_countries.fields.CountryField(max_length=2)),
                ('s_photo', models.ImageField(default='', upload_to='sharing/')),
                ('s_appreciation', models.CharField(default='', max_length=160)),
                ('s_video_talk', models.FileField(default='', upload_to='talk/')),
                ('s_video_dance', models.FileField(default='', upload_to='dance/')),
                ('s_date', models.DateField(auto_now=True)),
                ('s_location', models.CharField(max_length=30)),
                ('s_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
                ('s_teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['s_date'],
            },
        ),
        migrations.CreateModel(
            name='LikesToSharing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_type', models.CharField(choices=[('LO', 'love'), ('DO', 'dope'), ('IS', 'inspiring'), ('RS', 'respect'), ('CT', 'cute'), ('IF', 'informative'), ('EM', 'emotional')], default='LO', max_length=2)),
                ('l_liker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('l_shareid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_sharing', to='sharing.Sharing')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_comment', models.CharField(max_length=255)),
                ('c_commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('c_shareid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_sharing', to='sharing.Sharing')),
            ],
        ),
    ]
