# Generated by Django 2.2.3 on 2019-08-06 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arctowski_app', '0011_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='lala'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='scan',
            field=models.FileField(blank=True, null=True, upload_to='lolo'),
        ),
    ]
