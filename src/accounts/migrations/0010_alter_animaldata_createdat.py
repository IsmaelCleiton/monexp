# Generated by Django 4.2.6 on 2024-02-08 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_animaldata_size_remove_animaldata_weight_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animaldata',
            name='createdAt',
            field=models.DateField(default=datetime.datetime(2024, 2, 8, 14, 54, 45, 38918, tzinfo=datetime.timezone.utc)),
        ),
    ]
