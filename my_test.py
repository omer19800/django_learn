import os

os.environ["DJANGO_SETTINGS_MODULE"] = 'imdb.settings'

import django
django.setup()

from imdb_app.models import Movie

if __name__ == '__main__':
    print("sheesh")
