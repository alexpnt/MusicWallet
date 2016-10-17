from django import forms
from .models import Music,User
from django.forms import ModelForm

class UserForm(forms.ModelForm):
	"""Model form for an user
	"""
	class Meta:
		model = User
		fields = ('name', 'email','favourite_musics')

	def __init__(self, *args, **kwargs):
	    super(UserForm, self).__init__(*args, **kwargs)
	    self.fields['name'].required = True
	    self.fields['email'].required = True
	    self.fields['favourite_musics'].required = False

class MusicForm(forms.ModelForm):
	"""Model form for a music
	"""
	class Meta:
		model = Music
		fields = ('title', 'artist','album')

	def __init__(self, *args, **kwargs):
	    super(MusicForm, self).__init__(*args, **kwargs)
	    self.fields['title'].required = True
	    self.fields['artist'].required = True
	    self.fields['album'].required = True