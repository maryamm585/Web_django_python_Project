# Generated by Django 5.0.4 on 2024-05-09 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_user_isadmin_user_isuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isLogin',
            field=models.BooleanField(default=False),
        ),
    ]
