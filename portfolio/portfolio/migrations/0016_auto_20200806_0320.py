# Generated by Django 2.2.6 on 2020-08-06 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_auto_20200804_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milestone',
            name='m_context',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='sharing',
            name='s_photo_comment',
            field=models.ImageField(default='photo_comment.png', upload_to='sharing/'),
        ),
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_content', models.TextField(default='')),
                ('b_artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='biography', to='portfolio.Portfolio')),
            ],
        ),
    ]
