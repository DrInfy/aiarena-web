# Generated by Django 3.0.8 on 2020-11-03 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0117_news'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='date_created',
            new_name='created',
        ),
    ]