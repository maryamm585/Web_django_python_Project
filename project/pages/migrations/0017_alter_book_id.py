# Generated by Django 5.0.4 on 2024-05-13 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
