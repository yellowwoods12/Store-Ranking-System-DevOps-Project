# Generated by Django 3.0.5 on 2020-05-09 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locker', '0006_auto_20200509_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onboard',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
