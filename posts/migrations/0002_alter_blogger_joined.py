# Generated by Django 3.2.7 on 2023-08-13 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogger',
            name='joined',
            field=models.IntegerField(default=2023),
        ),
    ]
