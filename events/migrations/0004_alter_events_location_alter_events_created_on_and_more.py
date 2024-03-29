# Generated by Django 5.0.2 on 2024-03-06 13:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_events_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='Location',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='events',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 6, 13, 13, 8, 622343, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='events',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='events',
            name='status',
            field=models.CharField(choices=[('Upcoming', 'Upcoming'), ('Happening Now', 'Happening Now'), ('DONE', 'DONE')], default='Upcoming', max_length=30),
        ),
    ]
