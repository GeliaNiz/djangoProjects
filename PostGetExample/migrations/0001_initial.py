# Generated by Django 3.1.7 on 2021-03-06 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=30)),
                ('degree', models.CharField(max_length=30)),
                ('place', models.IntegerField()),
                ('date', models.CharField(max_length=30)),
            ],
        ),
    ]