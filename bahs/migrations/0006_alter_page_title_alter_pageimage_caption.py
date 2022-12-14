# Generated by Django 4.1.3 on 2022-11-15 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bahs', '0005_alter_page_body_alter_pageimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='pageimage',
            name='caption',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
    ]
