# Generated by Django 4.2.6 on 2023-12-08 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_laboratory_id_alter_researcher_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='researcher',
            name='accessLevel',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
