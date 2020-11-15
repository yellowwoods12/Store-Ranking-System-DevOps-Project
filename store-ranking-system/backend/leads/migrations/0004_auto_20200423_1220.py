# Generated by Django 3.0.5 on 2020-04-23 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_lead_addressfield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='addressfield',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='landmarksfield',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='lockerfield',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='query',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='zipfield',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
