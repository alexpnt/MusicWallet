from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from models import User,Music
from serializers import UserSerializer,MusicSerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from musicwalletapp.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import detail_route


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @detail_route(methods=['post'])
    def add_fav_music(self, request, pk):
        user = self.get_object()
        try:
        	music = get_object_or_404(Music, pk=pk)
	        user.favourite_musics.add(music)
	        user.save()
	        return Response({'status': 'Success: Favourite music added'})
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @detail_route(methods=['delete'])
    def remove_fav_music(self, request, pk):
        user = self.get_object()
        try:
        	music = get_object_or_404(Music, pk=pk)
	        user.favourite_musics.remove(music)
	        user.save()
	        return Response({'status': 'Success: Favourite music removed'})
        except:
        	return Response(status=status.HTTP_400_BAD_REQUEST)
        	
class MusicViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly,)
    serializer_class = MusicSerializer
    queryset = Music.objects.all()

    def perform_create(self, serializer):
    	serializer.save(created_by=self.request.user)

