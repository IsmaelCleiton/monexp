# Generated by Django 4.2.6 on 2024-02-08 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_animaldata_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animaldata',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
