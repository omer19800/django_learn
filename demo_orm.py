import os

os.environ["DJANGO_SETTINGS_MODULE"] = "imdb.settings"

import django
django.setup()

from imdb_app.models import *

if __name__ == '__main__':
    pass
    # movies = Movie.objects.all()
    # movies = Movie.objects.filter(name='inception')
    # movies = Movie.objects.filter(id=1)
    # for movie in movies:
    #     # print(movie.name, movie.description)
    #     print(movie)

    # movie = Movie.objects.filter(id=1)[0]
    # movie.year = 2010
    # movie.save()

    # movie = Movie.objects.get(id=2)
    # movie.year = 1994
    # movie.description = "Some new description"
    # movie.save()

    # movie = Movie(name="Titanic", year=2000)
    # movie.save()

    # Movie.objects.create(description="dhgdjgsd", year=2000)

    # m = Movie.objects.get(description="dhgdjgsd").delete()

    # Movie(description="dsfsdsdf").save()

    # m = Movie.objects.get(name='Pulp fiction')
    # print(m.director)

    # d = Director.objects.all()[0]
    # print(d.movie_set.all())

