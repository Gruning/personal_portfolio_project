# Generated by Django 3.1 on 2020-08-19 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_remove_project_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
