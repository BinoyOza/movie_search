# Generated by Django 3.2.13 on 2022-06-20 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_movie_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
