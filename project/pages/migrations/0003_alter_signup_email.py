# Generated by Django 5.0.4 on 2024-05-07 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_signup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
