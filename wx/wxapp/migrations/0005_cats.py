# Generated by Django 3.0.6 on 2020-11-15 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wxapp', '0004_auto_20201115_0009'),
    ]

    operations = [
        migrations.CreateModel(
            name='cats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=10)),
                ('character', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=300)),
                ('vet', models.IntegerField()),
                ('openid', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
            ],
        ),
    ]