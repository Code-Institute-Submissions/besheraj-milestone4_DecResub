# Generated by Django 3.1.2 on 2020-12-14 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20201111_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
