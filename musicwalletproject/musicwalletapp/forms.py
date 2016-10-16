from django import forms
from .models import Music
from django.forms import ModelForm

class MusicForm(forms.ModelForm):
	class Meta:
		model = Music
		fields = ('title', 'artist','album')