# Generated by Django 2.0.5 on 2018-05-09 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]