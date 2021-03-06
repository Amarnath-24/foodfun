# Generated by Django 3.0 on 2020-07-18 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=60)),
                ('recipe_type', models.IntegerField(choices=[(0, 'SelectType'), (1, 'Veg'), (2, 'Non Veg')], default=0)),
                ('ingredients', models.TextField()),
                ('procedure', models.TextField()),
            ],
            options={
                'db_table': 'Recipe',
            },
        ),
    ]
