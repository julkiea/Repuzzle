# Generated by Django 5.1 on 2024-09-01 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_alter_userprofile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
    ]
