from django import forms
from models import User,Music
from django.forms import ModelForm

class UserForm(forms.ModelForm):
	"""Model form for an user
	"""
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ('username', 'email','password')

	def save(self):
		user = User.objects.create_user(
		    username=self.cleaned_data['username'],
		    email=self.cleaned_data['email'])
		user.set_password(self.cleaned_data['password'])		#encrypt password
		user.save()
		return user


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