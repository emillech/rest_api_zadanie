# Generated by Django 3.1.6 on 2021-02-06 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(upload_to='images'),
        ),
    ]