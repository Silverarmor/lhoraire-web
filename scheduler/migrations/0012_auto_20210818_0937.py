# Generated by Django 3.1.6 on 2021-08-18 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0011_auto_20210814_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskinfo',
            name='gradient',
            field=models.CharField(choices=[['+', 'Increasing'], ['-', 'Decreasing'], ['0', 'Roughly same']], max_length=1, null=True),
        ),
    ]
