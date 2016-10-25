from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

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

	@receiver(post_save, sender=settings.AUTH_USER_MODEL)
	def create_auth_token(sender, instance=None, created=False, **kwargs):
		if created:
		    Token.objects.create(user=instance)