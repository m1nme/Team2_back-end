# Generated by Django 3.0.6 on 2020-12-03 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wxapp', '0013_feedbacks_urllist'),
    ]

    operations = [
        migrations.CreateModel(
            name='lastfeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catid', models.IntegerField()),
                ('time', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='feed',
            name='time',
            field=models.CharField(max_length=20),
        ),
    ]
