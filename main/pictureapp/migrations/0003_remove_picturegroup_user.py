# Generated by Django 3.0.3 on 2020-02-16 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictureapp', '0002_auto_20200216_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picturegroup',
            name='user',
        ),
    ]