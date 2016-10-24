from django.shortcuts import render,redirect,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from django.template import loader
from models import Music
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from serializers import UserSerializer,MusicSerializer
from forms import MusicForm,UserForm
from django.contrib.auth.mixins import LoginRequiredMixin

#################################
#								#
#	Function Based Views		#
#		Deprecated				#
#								#
#################################

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
			musics=Music.objects.all()
			for music in musics:
				if form.cleaned_data.get('title')==music.title and \
				form.cleaned_data.get('artist')==music.artist and \
				form.cleaned_data.get('album')==music.album:
					return render(request, edit_music_tpl, {'form': form})
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
			users=User.objects.all()
			for user in users:
				if form.cleaned_data.get('name')==user.name and form.cleaned_data.get('email')==user.email:
					return render(request, edit_usr_tpl, {'form': form})
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


#### REST API #### 

@api_view(['GET'])
def api_users(request,format=None):
	"""List users. Only the GET http verb is allowed.

	Keyword arguments: 
	request -- the HttpRequest
	format 	-- the output format
	"""
	if request.method == 'GET':
	    users = User.objects.all()
	    serializer = UserSerializer(users, many=True)
	    return Response(serializer.data)
	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def api_user_details(request,pk,format=None):
	"""Return the details of an user. Only the GET http verb is allowed.
	
	Keyword arguments: 
	request -- the HttpRequest
	pk 		-- the Primary Key of the desired user 
	format 	-- the output format
	"""
	if request.method == 'GET':
		try:
			user = get_object_or_404(User, pk=pk)
		except:
			return HttpResponse(status=status.HTTP_404_NOT_FOUND)

		serializer = UserSerializer(user)
		return Response(serializer.data)
	return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def api_user_new(request,format=None):
	"""Create a new user. Only the POST http verb is allowed.

	Keyword arguments: 
	request -- the HttpRequest
	format 	-- the output format
	"""
	if request.method == 'POST':
		serializer=UserSerializer(data=request.data)
		if serializer.is_valid():
			users=User.objects.all()
			for user in users:
				if serializer.validated_data['name']==user.name \
				and serializer.validated_data['email']==user.email:
					return Response(status=status.HTTP_201_CREATED)
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def api_user_edit(request,pk,format=None):
	"""Edit the details of an user. Only the PUT http verb is allowed.
	
	Keyword arguments: 
	request -- the HttpRequest
	pk 		-- the Primary Key of the desired user 
	format 	-- the output format
	"""
	if request.method == 'PUT':
		try:
			user = get_object_or_404(User, pk=pk)
		except:
			return HttpResponse(status=status.HTTP_404_NOT_FOUND)

		serializer=UserSerializer(user,data=request.data,partial=True)
		if serializer.is_valid():
		    serializer.save()
		    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def api_user_delete(request,pk,format=None):
	"""Delete an user. Only the DELETE http verb is allowed.
	
	Keyword arguments: 
	request -- the HttpRequest
	pk 		-- the Primary Key of the desired user 
	format 	-- the output format
	"""
	if request.method == 'DELETE':
		try:
			user = get_object_or_404(User, pk=pk)
		except:
			return HttpResponse(status=status.HTTP_404_NOT_FOUND)

		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def api_musics(request,format=None):
	"""List musics. Only the GET http verb is allowed.
	
	Keyword arguments: 
	request -- the HttpRequest
	format 	-- the output format
	"""
	if request.method == 'GET':
	    musics = Music.objects.all()
	    serializer = MusicSerializer(musics,many=True)
	    return Response(serializer.data)
	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def api_music_details(request,pk,format=None):
	"""Return the details of a music. Only the GET http verb is allowed.
	
	Keyword arguments: 
	request -- the HttpRequest
	pk 		-- the Primary Key of the desired music 
	format 	-- the output format
	"""
	if request.method == 'GET':
		try:
			music = get_object_or_404(Music, pk=pk)
		except:
			return HttpResponse(status=status.HTTP_404_NOT_FOUND)

		serializer = MusicSerializer(music)
		return Response(serializer.data)
	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def api_music_new(request,format=None):
	"""Create a new music. Only the POST http verb is allowed.

	Keyword arguments: 
	request -- the HttpRequest
	format 	-- the output format
	"""
	if request.method == 'POST':
		serializer=MusicSerializer(data=request.data)
		if serializer.is_valid():
			musics=Music.objects.all()
			for music in musics:
				if serializer.validated_data['title']==music.title \
				and serializer.validated_data['artist']==music.artist \
				and serializer.validated_data['album']==music.album:
					return Response(status=status.HTTP_201_CREATED)
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def api_music_edit(request,pk,format=None):
	"""Edit the details of music. Only the PUT http verb is allowed.
	
	Keyword arguments: 
	request -- the HttpRequest
	pk 		-- the Primary Key of the desired music 
	format 	-- the output format
	"""
	if request.method == 'PUT':
		try:
			music = get_object_or_404(Music, pk=pk)
		except:
			return HttpResponse(status=status.HTTP_404_NOT_FOUND)

		serializer=MusicSerializer(music,data=request.data,partial=True)
		if serializer.is_valid():
		    serializer.save()
		    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def api_music_delete(request,pk,format=None):
	"""Delete a music. Only the DELETE http verb is allowed.
	
	Keyword arguments: 
	request -- the HttpRequest
	pk 		-- the Primary Key of the desired music 
	format 	-- the output format
	"""
	if request.method == 'DELETE':
		try:
			music = get_object_or_404(Music, pk=pk)
		except:
			return HttpResponse(status=status.HTTP_404_NOT_FOUND)

		music.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE'])
def api_favourite_music(request,pk1,pk2,format=None):
	"""Add a music to the list of favourite musics of an user. 
	Only the PUT and DELETE http verb are allowed.
	
	Keyword arguments: 
	request 	-- the HttpRequest
	pk1 		-- the Primary Key of the desired music
	pk2 		-- the Primary Key of the desired user 
	format 		-- the output format
	"""
	if request.method == 'PUT':
		try:
			music = get_object_or_404(Music, pk=pk1)
			user = get_object_or_404(User, pk=pk2)
		except:
			return HttpResponse(status=status.HTTP_404_NOT_FOUND)

		user.favourite_musics.add(music)
		user.save()
		return Response(status=status.HTTP_202_ACCEPTED)

	elif request.method == 'DELETE':
		try:
			music = get_object_or_404(Music, pk=pk1)
			user = get_object_or_404(User, pk=pk2)
		except:
			return HttpResponse(status=status.HTTP_404_NOT_FOUND)

		user.favourite_musics.remove(music)
		user.save()
		return Response(status=status.HTTP_202_ACCEPTED)
	return Response(status=status.HTTP_400_BAD_REQUEST)