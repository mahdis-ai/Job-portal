# Generated by Django 3.2.7 on 2022-07-29 13:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0004_auto_20220729_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 29, 17, 46, 6, 948746)),
        ),
    ]
