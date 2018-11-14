import django_filters
from .models import MovieInfo

class MovieInfoFilter(django_filters.FilterSet):

    class Meta:
        model = MovieInfo
        fields = {
            'movie_name' : ['icontains'],
            'movie_review' : ['icontains'],
            'movie_release_date' : ['icontains']
        }
       