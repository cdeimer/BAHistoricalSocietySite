# Generated by Django 4.1.3 on 2022-12-05 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bahs', '0006_alter_page_title_alter_pageimage_caption'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='bahs.page')),
            ],
        ),
    ]
