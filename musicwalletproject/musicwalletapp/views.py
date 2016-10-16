from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from musicwalletapp.models import Music,User

def index(request):
	template = loader.get_template('musicwalletapp/index.html')
	musics=Music.objects.all()
	users=User.objects.all()
	context={'musics':musics,'users':users}

	return render(request, 'musicwalletapp/index.html', context)
