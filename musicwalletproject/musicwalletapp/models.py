from __future__ import unicode_literals

from django.db import models

class Music(models.Model):
	"""Data model of a music
	"""
	title = models.CharField(max_length=200)
	artist = models.CharField(max_length=200)
	album = models.CharField(max_length=200)

	def __str__(self):
	    return self.title

class User(models.Model):
	"""Data model of a user
	"""
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	favourite_musics = models.ManyToManyField(Music, blank=True)

	def __str__(self):
	    return self.title