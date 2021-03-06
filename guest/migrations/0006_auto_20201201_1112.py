# Generated by Django 3.1.1 on 2020-12-01 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0005_auto_20201201_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestworker',
            name='AdharNumber',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='guestworker',
            name='District',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='guestworker',
            name='IDproof',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='guestworker',
            name='PermanantAddress',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='guestworker',
            name='Photo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='guestworker',
            name='Qualification',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='guestworker',
            name='State',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='guestworker',
            name='TemporaryAddress',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='guestworker',
            name='dob',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='guestworker',
            name='gender',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
