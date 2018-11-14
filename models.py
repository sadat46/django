from django.db import models

class MovieInfo(models.Model):
	movie_name = models.CharField(max_length=200)
	movie_review = models.CharField(max_length=5)
	movie_release_date = models.CharField(max_length=35)
	movie_type = models.CharField(max_length=200)
	movie_details = models.TextField(max_length=200)
	

	def __str__(self):
		return self.movie_name

	class Meta:
		ordering = ('movie_name',)


class SongInfo(models.Model):
	song_name = models.CharField(max_length=200)
	singer_name = models.CharField(max_length=200)
	album_name = models.CharField(max_length=200)
	

	def __str__(self):
		return self.song_name

