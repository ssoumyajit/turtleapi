# Generated by Django 2.2.6 on 2020-08-04 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_auto_20200731_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharing',
            name='s_photo_comment',
            field=models.ImageField(default='photo_comment.png', upload_to='sharing/comment/'),
        ),
        migrations.AlterField(
            model_name='sharing',
            name='s_student',
            field=models.ManyToManyField(related_name='mystudent', to='portfolio.Portfolio'),
        ),
        migrations.AlterField(
            model_name='sharing',
            name='s_teacher',
            field=models.ManyToManyField(related_name='myteacher', to='portfolio.Portfolio'),
        ),
    ]
