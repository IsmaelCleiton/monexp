# Generated by Django 4.2.6 on 2023-11-23 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_researcher_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratory',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='researcher',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
