from rest_framework import serializers
from models import User,Music


class MusicSerializer(serializers.ModelSerializer):
	created_by = serializers.ReadOnlyField(source='created_by.username')

	class Meta:
	    model = Music
	    fields = ('id','title', 'artist','album','created_by')

class UserSerializer(serializers.ModelSerializer):
	favourite_musics = MusicSerializer(read_only=True,many=True,required=False)
	email = serializers.EmailField(required=True)

	class Meta:
	    model = User
	    fields = ('id','username', 'email','password','favourite_musics')

	def create(self, validated_data):
		user = User(username=validated_data['username'],email=validated_data['email'])
		user.set_password(validated_data['password'])
		user.save()
		return user

	def update(self, instance, validated_data):
		instance.username = validated_data.get('username', instance.username)
		instance.email = validated_data.get('email', instance.email)
		instance.set_password(validated_data.get('password', instance.password))
		instance.save()
		return instance