# Generated by Django 4.1.3 on 2022-11-12 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bahs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageimage',
            name='caption',
            field=models.TextField(default=None),
        ),
    ]