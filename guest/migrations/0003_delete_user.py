# Generated by Django 3.1.1 on 2020-11-24 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
