from django import forms

from .models import MovieInfo


class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieInfo 
        fields = [
            'movie_name',
	        'movie_review', 
	        'movie_release_date' ,
	        'movie_type',
	        'movie_details' ,
            
            ]
