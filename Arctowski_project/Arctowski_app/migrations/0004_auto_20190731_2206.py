# Generated by Django 2.2.3 on 2019-07-31 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arctowski_app', '0003_auto_20190731_2200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incase',
            name='sum_of_value',
        ),
        migrations.AddField(
            model_name='case',
            name='sum_of_value',
            field=models.DecimalField(decimal_places=2, max_digits=13, null=True),
        ),
    ]
