# Generated by Django 2.2 on 2021-01-20 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_recipe_process_val'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='process_val',
        ),
    ]
