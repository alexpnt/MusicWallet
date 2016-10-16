from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from musicwalletapp.models import Music,User
from .forms import MusicForm

def index(request):
	template = loader.get_template('musicwalletapp/index.html')
	musics=Music.objects.all()
	users=User.objects.all()
	context={'musics':musics,'users':users}

	return render(request, 'musicwalletapp/index.html', context)

def music_new(request):
	if request.method == "POST":
		form = MusicForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = MusicForm(None)
		return render(request, 'musicwalletapp/music_edit.html', {'form': form})

def music_edit(request, pk):
	try:
		music = get_object_or_404(Music, pk=pk)
	except:
		form = MusicForm(None)
		return render(request,'musicwalletapp/music_edit.html',{'form': form,'error_message': "The desired music does not exist. Create a new one"})
	
	if request.method == "POST":
	    form = MusicForm(request.POST, instance=music)
	    if form.is_valid():
	        form.save()
	        return redirect('index')
	else:
	    form = MusicForm(instance=music)
	return render(request, 'musicwalletapp/music_edit.html', {'form': form})

def music_delete(request,pk):
	try:
		music = get_object_or_404(Music, pk=pk)
	except:
		return redirect('index')
	
	music.delete()
	return redirect('index')









