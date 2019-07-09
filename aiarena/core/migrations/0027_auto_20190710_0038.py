# Generated by Django 2.1.7 on 2019-07-09 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20190706_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='type',
            field=models.CharField(choices=[('MatchCancelled', 'MatchCancelled'), ('InitializationError', 'InitializationError'), ('Timeout', 'Timeout'), ('ProcessingReplay', 'ProcessingReplay'), ('Player1Win', 'Player1Win'), ('Player1Crash', 'Player1Crash'), ('Player1TimeOut', 'Player1TimeOut'), ('Player2Win', 'Player2Win'), ('Player2Crash', 'Player2Crash'), ('Player2TimeOut', 'Player2TimeOut'), ('Tie', 'Tie'), ('Error', 'Error')], max_length=32),
        ),
    ]
