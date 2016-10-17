from django import forms
from .models import Music,User
from django.forms import ModelForm

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('name', 'email','favourite_musics')

class MusicForm(forms.ModelForm):
	class Meta:
		model = Music
		fields = ('title', 'artist','album')