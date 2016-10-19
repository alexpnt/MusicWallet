from rest_framework import serializers
from models import User,Music



class MusicSerializer(serializers.ModelSerializer):
	class Meta:
	    model = Music
	    fields = ('id','title', 'artist','album')

class UserSerializer(serializers.ModelSerializer):
	favourite_musics = MusicSerializer(read_only=True,many=True,required=False)

	class Meta:
	    model = User
	    fields = ('id','name', 'email','favourite_musics')

	def create(self, validated_data):
		user = User.objects.create(**validated_data)
		return user