# Generated by Django 3.0 on 2021-06-09 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210609_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='avaragerating',
            field=models.FloatField(default=0),
        ),
    ]
