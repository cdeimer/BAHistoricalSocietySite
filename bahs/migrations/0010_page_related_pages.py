# Generated by Django 4.1.3 on 2022-12-05 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bahs', '0009_rename_pagetags_pagetag'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='related_pages',
            field=models.ManyToManyField(blank=True, to='bahs.page'),
        ),
    ]
