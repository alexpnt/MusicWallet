from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

class Music(models.Model):
	"""Data model of a music
	"""
	title = models.CharField(max_length=200)
	artist = models.CharField(max_length=200)
	album = models.CharField(max_length=200)
	created_by = models.ForeignKey('User', related_name='musics',null=True)

	def __str__(self):
	    return self.title

class User(AbstractUser):
	"""Data model of an user
	"""
	favourite_musics = models.ManyToManyField(Music, blank=True)

	def __str__(self):
	    return self.user