# Generated by Django 4.0.3 on 2022-03-27 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_hour_busynesslevel'),
    ]

    operations = [
        migrations.AddField(
            model_name='hour',
            name='hourofDay',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]