# Generated by Django 5.1 on 2024-08-21 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_puzzle_priority'),
    ]

    operations = [
        migrations.RenameField(
            model_name='puzzle',
            old_name='priority',
            new_name='condition',
        ),
    ]
