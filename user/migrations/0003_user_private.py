# Generated by Django 4.0.6 on 2022-07-31 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='private',
            field=models.BooleanField(default=False),
        ),
    ]
