# Generated by Django 5.1 on 2024-08-25 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_puzzle_image_delete_puzzleimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puzzle',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='website.category'),
        ),
    ]
