from django.shortcuts import render,redirect,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from django.template import loader
from models import Music,User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from serializers import UserSerializer,MusicSerializer

from django.http import HttpResponseRedirect
from forms import MusicForm,UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,View,ListView,FormView,UpdateView,CreateView,DeleteView
from django.views.generic.edit import ProcessFormView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.core.exceptions import PermissionDenied

index_tpl="musicwalletapp/index.html"
edit_music_tpl="musicwalletapp/music_edit.html"
edit_usr_tpl="musicwalletapp/user_edit.html"

#################################
#								#
#	Class Based Views			#
#								#
#################################

class LandPageView(TemplateView):
	template_name = "musicwalletapp/landpage.html"

	def get(self, request, *args, **kwargs):
		if self.request.user.is_authenticated():
			return HttpResponseRedirect(reverse_lazy('dashboard'))
		else:
			return render(request, self.template_name)

class SignInView(TemplateView):
	"""
	View used to sign in an user
	"""
	template_name = "musicwalletapp/landpage.html"

	def post(self, request, *args, **kwargs):
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		#check credentials
		user = authenticate(username=username,password=password)	
		if user:
			#attach user to the current session
			login(request,user)
			msg="Your are now signed in! Welcome!"
			messages.add_message(request, messages.SUCCESS, msg)
			#redirect to dashboard															
			return HttpResponseRedirect(reverse_lazy('dashboard'))
		else:
			msg="Username or password is incorrect. Please try again."
			messages.add_message(request, messages.ERROR, msg)
			return HttpResponseRedirect(reverse_lazy('landpage'))

class SignUpView(TemplateView):
	"""
	View used to create and sign in a new user
	"""
	template_name = "musicwalletapp/landpage.html"

	def post(self, request, *args, **kwargs):
		userform = UserForm(request.POST)
		username = request.POST.get('username')
		existing_user = User.objects.filter(username__exact=username)
		
		if not existing_user and userform.is_valid():
			userform.save()
			#check credentials
			user = authenticate(username=username,password=request.POST.get('password'))	
			#attach to the current session
			login(request,user)
			msg="Your are now signed in! Welcome!"
			messages.add_message(request, messages.SUCCESS, msg)
			#redirect to dashboard															
			return HttpResponseRedirect(reverse_lazy('dashboard'))
		elif existing_user:
			msg="Username already in use! Please, choose another."
			messages.add_message(request, messages.WARNING, msg)
			return HttpResponseRedirect(reverse_lazy('landpage'))
		else:
			msg="An error has occurred. Please try again."
			messages.add_message(request, messages.ERROR, msg)
			return HttpResponseRedirect(reverse_lazy('landpage'))


class SignOutView(LoginRequiredMixin,TemplateView):
	"""
	View used to logout an user and clear his session data
	"""
	template_name = "musicwalletapp/landpage.html"

	def get(self, request, *args, **kwargs):
		logout(request)
		msg="Signed Out!"
		messages.add_message(request, messages.SUCCESS, msg)
		return HttpResponseRedirect(reverse_lazy('landpage'))

class DashboardView(LoginRequiredMixin,ListView):
	"""
	View used to display the list of favourites musics from an user
	"""
	template_name = "musicwalletapp/dashboard.html"
	model=Music
	paginate_by = 5
	context_object_name = 'favourite_musics'

	def get_queryset(self):
		return Music.objects.filter(user=self.request.user.id)

class MusicListView(LoginRequiredMixin,ListView):
	"""
	View to get a list of musics that are not favourite
	"""
	template_name = "musicwalletapp/musics.html"
	model=Music
	paginate_by = 10
	context_object_name = 'musics'

	def get_queryset(self):
		return Music.objects.exclude(user__id=self.request.user.id) 


class AddDelFavMusicView(LoginRequiredMixin,View):
	"""
	View to add or remove favourite musics from an existing user
	"""
	def post(self, request, **kwargs):
		music_id = self.kwargs.get('pk')
		user = self.request.user

		music = get_object_or_404(Music, pk=music_id)
		user.favourite_musics.add(music)
		user.save()

		return HttpResponseRedirect(reverse_lazy('music_list'))

	def get(self, request, **kwargs):
		music_id = self.kwargs.get('pk')
		user = self.request.user

		music = get_object_or_404(Music, pk=music_id)
		user.favourite_musics.remove(music)
		user.save()

		return HttpResponseRedirect(reverse_lazy('dashboard'))

class AccountView(LoginRequiredMixin,TemplateView):
	"""
	View used to display user details
	"""
	template_name = "musicwalletapp/user_edit.html"

	def get_context_data(self, **kwargs):
		context = super(AccountView, self).get_context_data(**kwargs)
		user = self.request.user
		context['user']=user
		return context

class UpdateAccountView(LoginRequiredMixin,View):
	"""
	View used to update an user
	"""

	def post(self, request, *args, **kwargs):
		user = User.objects.get(id=self.request.user.id)
		user.username = request.POST.get('username')
		user.email = request.POST.get('email')
		user.set_password = request.POST.get('password')
		user.save()

		msg="Account details updated."
		messages.add_message(request, messages.SUCCESS, msg)
		return HttpResponseRedirect(reverse_lazy('dashboard'))

class DeleteAccountView(LoginRequiredMixin,DeleteView):
	"""
	View used to delete an user
	"""
	model = User
	success_url = reverse_lazy('signout')

	def get_context_data(self, **kwargs):
		context = super(DeleteAccountView, self).get_context_data(**kwargs)
		msg="Account Deleted."
		messages.add_message(self.request, messages.SUCCESS, msg)
		return context


class AddMusicView(LoginRequiredMixin,CreateView):
	"""
	View used to create a new music
	"""
	model=Music
	fields = ['title','artist','album']
	success_url = reverse_lazy('music_list')

	def form_valid(self, form):
		if form.is_valid():
			music=form.save(commit=False)
			music.created_by=self.request.user 				#associate to creator user
			music.save()
		return super(AddMusicView, self).form_valid(form)

class UpdateMusicView(LoginRequiredMixin,UpdateView):
	"""
	View used to update an existing music
	"""
	model=Music
	template_name= "musicwalletapp/music_edit.html"
	form_class=MusicForm
	success_url = reverse_lazy('music_list')

	def get_context_data(self, **kwargs):
		context = super(UpdateMusicView, self).get_context_data(**kwargs)
		music_id = self.kwargs.get('pk')
		music=Music.objects.get(id=music_id)
		context['form'] = self.form_class(instance=music)
		return context

	def get_object(self, *args, **kwargs):
		music = super(UpdateMusicView, self).get_object(*args, **kwargs)
		if music.created_by != self.request.user:
			msg="Sorry, you are not allowed to do that."
			messages.add_message(self.request, messages.WARNING, msg)
			raise PermissionDenied("Sorry, you are not allowed to do that.")
		return music


class DeleteMusicView(LoginRequiredMixin,DeleteView):
	"""
	View used to delete an existing music
	"""
	model = Music
	success_url = reverse_lazy('music_list')

	def get_object(self, *args, **kwargs):
		music = super(DeleteMusicView, self).get_object(*args, **kwargs)
		if music.created_by != self.request.user:
			msg="Sorry, you are not allowed to do that."
			messages.add_message(self.request, messages.WARNING, msg)
			raise PermissionDenied("Sorry, you are not allowed to do that.")
		return music








