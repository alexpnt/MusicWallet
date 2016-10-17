from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from musicwalletapp.models import Music,User
from .forms import MusicForm,UserForm

index_tpl="musicwalletapp/index.html"
edit_music_tpl="musicwalletapp/music_edit.html"
edit_usr_tpl="musicwalletapp/user_edit.html"

def index(request):
	"""Return the home page with a listing of users and musics.

	Keyword arguments: 
	request -- the HttpRequest
	"""
	template = loader.get_template(index_tpl)
	musics=Music.objects.all()
	users=User.objects.all()
	context={'musics':musics,'users':users}

	return render(request, index_tpl, context)

def music_new(request):
	"""Return an empty form 
	and redirect to the homepage after the music form is validated and saved.
	
	Keyword arguments: 
	request -- the HttpRequest
	"""
	if request.method == "POST":									#save the new submitted data
		form = MusicForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('index')
		return render(request, edit_music_tpl, {'form': form})
	else:															#first time access
		form = MusicForm(None)
		return render(request, edit_music_tpl, {'form': form})

def music_edit(request, pk):
	"""Return a form populated with data from the desired music 
	and redirect to the homepage after the music form is validated and saved.

	Keyword arguments: 
	request -- the HttpRequest
	pk 		-- the Primary Key of the desired music 
	"""
	try:
		music = get_object_or_404(Music, pk=pk)						#obtain the desired music  
	except:
		form = MusicForm(None)										#create a new form in case of failure
		return render(request,edit_music_tpl,{'form': form,
			'error_message': "The desired music does not exist. Create a new one."})
	
	if request.method == "POST":									#save the new submitted data
	    form = MusicForm(request.POST, instance=music)
	    if form.is_valid():
	        form.save()
	        return redirect('index')
	    return render(request, edit_music_tpl, {'form': form})
	else:
	    form = MusicForm(instance=music)
	    return render(request, edit_music_tpl, {'form': form})

def music_delete(request,pk):
	"""Delete the desired music and return to the homepage.
	
	Keyword arguments: 
	request -- the HttpRequest
	pk 		-- the Primary Key of the desired music 
	"""
	try:
		music = get_object_or_404(Music, pk=pk)					
	except:
		return redirect('index')
	
	music.delete()
	return redirect('index')

def user_new(request):
	"""Return an empty form and redirect to the homepage after the user form is validated and saved.
	
	Keyword arguments: 
	request -- the HttpRequest
	"""
	if request.method == "POST":									#save the new submitted data
		form = UserForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('index')
		return render(request, edit_usr_tpl, {'form': form})
	else:															#first time access
		form = UserForm(None)
		return render(request, edit_usr_tpl, {'form': form})

def user_edit(request, pk):
	"""Return a form populated with data from the desired user 
	and redirect to the homepage after the user form is validated and saved.

	Keyword arguments: 
	request -- the HttpRequest
	pk 		-- the Primary Key of the desired user 
	"""
	try:
		user = get_object_or_404(User, pk=pk)						#obtain the desired music 
	except:
		form = UserForm(None)										#create a new form in case of failure
		return render(request,edit_usr_tpl,{'form': form,
			'error_message': "The desired user does not exist. Create a new one."})
	
	if request.method == "POST":									#save the new submitted data
	    form = UserForm(request.POST, instance=user)
	    if form.is_valid():
	        form.save()
	        return redirect('index')
	    return render(request, edit_usr_tpl, {'form': form})
	else:
	    form = UserForm(instance=user)
	    return render(request, edit_usr_tpl, {'form': form})

def user_delete(request,pk):
	"""Delete the desired user and return to the homepage.
	
	Keyword arguments: 
	request -- the HttpRequest
	pk 		-- the Primary Key of the desired user 
	"""
	try:
		user = get_object_or_404(User, pk=pk)
	except:
		return redirect('index')
	
	user.delete()
	return redirect('index')









