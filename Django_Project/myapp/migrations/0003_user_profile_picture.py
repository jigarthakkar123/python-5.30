# Generated by Django 5.0.6 on 2024-06-01 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default='', upload_to='profile_picture/'),
        ),
    ]
