# Generated by Django 4.1.3 on 2022-12-05 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bahs', '0007_pagetags'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='page_type',
            field=models.CharField(choices=[('Article', 'Article'), ('Album', 'Album'), ('Interview', 'Interview')], default='Article', max_length=10),
        ),
    ]
