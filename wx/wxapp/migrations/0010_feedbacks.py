# Generated by Django 3.0.6 on 2020-11-22 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wxapp', '0009_auto_20201122_2320'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedbacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=50)),
                ('catid', models.IntegerField(null=True)),
                ('postid', models.IntegerField(null=True)),
                ('commentid', models.IntegerField(null=True)),
                ('feedbacktype', models.IntegerField()),
                ('content', models.CharField(max_length=300)),
                ('answer', models.CharField(max_length=300, null=True)),
                ('vet', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
