# Generated by Django 2.1.7 on 2020-01-03 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0083_auto_20200101_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchparticipation',
            name='starting_elo',
            field=models.SmallIntegerField(null=True),
        ),
    ]
