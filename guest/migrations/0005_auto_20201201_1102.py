# Generated by Django 3.1.1 on 2020-12-01 05:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('guest', '0004_mca'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user_info',
            new_name='GuestWorker',
        ),
    ]
