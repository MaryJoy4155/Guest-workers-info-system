# Generated by Django 3.1.1 on 2020-12-01 05:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('guest', '0006_auto_20201201_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=200, null=True)),
                ('dob', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(blank=True, max_length=200, null=True)),
                ('PermanantAddress', models.CharField(blank=True, max_length=200, null=True)),
                ('TemporaryAddress', models.CharField(blank=True, max_length=200, null=True)),
                ('District', models.CharField(blank=True, max_length=200, null=True)),
                ('State', models.CharField(blank=True, max_length=200, null=True)),
                ('Qualification', models.CharField(blank=True, max_length=200, null=True)),
                ('AdharNumber', models.CharField(blank=True, max_length=200, null=True)),
                ('IDproof', models.CharField(blank=True, max_length=200, null=True)),
                ('Photo', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=200, null=True)),
                ('dob', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(blank=True, max_length=200, null=True)),
                ('PermanantAddress', models.CharField(blank=True, max_length=200, null=True)),
                ('TemporaryAddress', models.CharField(blank=True, max_length=200, null=True)),
                ('District', models.CharField(blank=True, max_length=200, null=True)),
                ('State', models.CharField(blank=True, max_length=200, null=True)),
                ('Qualification', models.CharField(blank=True, max_length=200, null=True)),
                ('AdharNumber', models.CharField(blank=True, max_length=200, null=True)),
                ('IDproof', models.CharField(blank=True, max_length=200, null=True)),
                ('Photo', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Mca',
        ),
    ]