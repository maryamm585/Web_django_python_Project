# Generated by Django 5.0.4 on 2024-05-13 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
