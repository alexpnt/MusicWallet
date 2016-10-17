from django import forms
from .models import Music,User
from django.forms import ModelForm

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('name', 'email','favourite_musics')

	def __init__(self, *args, **kwargs):
	    super(UserForm, self).__init__(*args, **kwargs)
	    self.fields['favourite_musics'].required = False

class MusicForm(forms.ModelForm):
	class Meta:
		model = Music
		fields = ('title', 'artist','album')