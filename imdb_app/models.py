from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


###makemigrations creates a ""plan"" for the execution
###sqlmigrate imdb_app 000file - shows the sql script that will be done
### migrate imdb_app executes the change

# Create your models here.

class Movie(models.Model):

    movie_name = models.CharField(null=False, blank=False, max_length=256)
    description = models.TextField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)

    director = models.ForeignKey('Director', on_delete=models.RESTRICT, null=True, blank=True)

    def __str__(self):
        return f"id: {self.id}, name: {self.name}"

    class Meta:
        db_table = 'Movies'


class Director(models.Model):

    name = models.CharField(null=False, blank=False, max_length=128)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"id: {self.id}, name: {self.name}"

    class Meta:
        db_table = 'Directors'

class Review(models.Model): #cant be null
    rating = models.FloatField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(10)])
    review_date = models.DateField(null=True, blank=True)
    review_text = models.TextField(null=True, blank=True, max_length=1024)
    movie = models.ForeignKey('Movie', on_delete=models.RESTRICT, null=True, blank=True)

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, rating: {self.rating}"

    class Meta:
        db_table = 'reviews'