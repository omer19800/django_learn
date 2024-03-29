# Generated by Django 4.1.7 on 2023-03-20 19:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("imdb_app", "0006_director_movie_director"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "rating",
                    models.PositiveIntegerField(
                        blank=True,
                        max_length=2,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(10),
                        ],
                    ),
                ),
                ("review_date", models.DateField(blank=True, null=True)),
                (
                    "review_text",
                    models.TextField(blank=True, max_length=1024, null=True),
                ),
                (
                    "movie",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="imdb_app.movie",
                    ),
                ),
            ],
        ),
    ]
