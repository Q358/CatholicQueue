# Generated by Django 4.0.3 on 2022-03-31 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0005_rename_hourofday_hour_hourofday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='week',
            name='weekStartDay',
        ),
        migrations.AddField(
            model_name='hour',
            name='isOpen',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]