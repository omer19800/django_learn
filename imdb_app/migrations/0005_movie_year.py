# Generated by Django 4.1.7 on 2023-03-20 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("imdb_app", "0004_remove_movie_name_movie_movie_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="year",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]