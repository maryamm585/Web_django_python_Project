# Generated by Django 5.0.4 on 2024-05-14 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_alter_book_description_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
