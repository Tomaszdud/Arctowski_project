# Generated by Django 2.2.3 on 2019-08-04 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Arctowski_app', '0009_auto_20190804_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incase',
            name='case',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Arctowski_app.Case'),
        ),
        migrations.AlterField(
            model_name='incase',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True),
        ),
    ]
