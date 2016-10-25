from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from musicwalletapp.models import User,Music
from musicwalletapp.serializers import UserSerializer,MusicSerializer

# '''
# 	User - Unit tests
# '''
# class GetUserListTest(APITestCase):
# 	def setUp(self):
# 		self.user = User.objects.create(name="John",email='john@doe.com')


# 	def test_get_user_list(self):
# 		"""
# 		Test wheter we can get a list of users.
# 		"""
# 		url = reverse('api_users')
# 		response = self.client.get(url)
# 		self.assertEqual(response.status_code, status.HTTP_200_OK)

# class GetUserTest(APITestCase):
# 	def setUp(self):
# 		self.user = User.objects.create(name="John",email='john@doe.com')


# 	def test_get_user(self):
# 		"""
# 		Test wheter we can get a new user.
# 		"""
# 		url = reverse('api_user_details',kwargs={'pk':self.user.id})
# 		response = self.client.get(url)
# 		self.assertEqual(response.status_code, status.HTTP_200_OK)

# class CreateUserTest(APITestCase):
# 	def setUp(self):
# 		self.data = {'name': 'John','email':'john@doe.com'}


# 	def test_create_user(self):
# 		"""
# 		Test wheter we can create a new user.
# 		"""
# 		url = reverse('api_user_new')
# 		response = self.client.post(url,self.data,format='json')
# 		self.assertEqual(response.status_code, status.HTTP_201_CREATED)



# class EditUserTest(APITestCase):
# 	def setUp(self):
# 		self.user = User.objects.create(name="John",email='john@doe.com')
# 		self.data = UserSerializer(self.user).data
# 		self.data.update({'name': 'Joe'})


# 	def test_edit_user(self):
# 		"""
# 		Test wheter we can edit an existing user.
# 		"""
# 		url = reverse('api_user_edit',kwargs={'pk':self.user.id})
# 		response = self.client.put(url,self.data,format='json')
# 		self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

# class DeleteUserTest(APITestCase):
# 	def setUp(self):
# 		self.user = User.objects.create(name="John",email='john@doe.com')


# 	def test_delete_user(self):
# 		"""
# 		Test wheter we can delete an existing user.
# 		"""
# 		url = reverse('api_user_delete',kwargs={'pk':self.user.id})
# 		response = self.client.delete(url)
# 		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

# '''
# 	Music - Unit tests
# '''
# class GetMusicListTest(APITestCase):
# 	def setUp(self):
# 		self.music = Music.objects.create(title="hola",artist="John",album='languages')


# 	def test_get_music_list(self):
# 		"""
# 		Test wheter we can get a list of musics.
# 		"""
# 		url = reverse('api_musics')
# 		response = self.client.get(url)
# 		self.assertEqual(response.status_code, status.HTTP_200_OK)

# class GetMusicTest(APITestCase):
# 	def setUp(self):
# 		self.music = Music.objects.create(title="hola",artist="John",album='languages')


# 	def test_get_music(self):
# 		"""
# 		Test wheter we can get a new music.
# 		"""
# 		url = reverse('api_music_details',kwargs={'pk':self.music.id})
# 		response = self.client.get(url)
# 		self.assertEqual(response.status_code, status.HTTP_200_OK)

# class CreateMusicTest(APITestCase):
# 	def setUp(self):
# 		self.data = {'title': 'hola','artist':'John','album':'languages'}


# 	def test_create_music(self):
# 		"""
# 		Test wheter we can create a new music.
# 		"""
# 		url = reverse('api_music_new')
# 		response = self.client.post(url,self.data,format='json')
# 		self.assertEqual(response.status_code, status.HTTP_201_CREATED)



# class EditMusicTest(APITestCase):
# 	def setUp(self):
# 		self.music = Music.objects.create(title="hola",artist="John",album='languages')
# 		self.data = MusicSerializer(self.music).data
# 		self.data.update({'title': 'salut'})


# 	def test_edit_music(self):
# 		"""
# 		Test wheter we can edit an existing music.
# 		"""
# 		url = reverse('api_music_edit',kwargs={'pk':self.music.id})
# 		response = self.client.put(url,self.data,format='json')
# 		self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

# class DeleteMusicTest(APITestCase):
# 	def setUp(self):
# 		self.music = Music.objects.create(title="hola",artist="John",album='languages')


# 	def test_delete_music(self):
# 		"""
# 		Test wheter we can delete an existing music.
# 		"""
# 		url = reverse('api_music_delete',kwargs={'pk':self.music.id})
# 		response = self.client.delete(url)
# 		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


# class AddFavouriteMusicTest(APITestCase):
# 	def setUp(self):
# 		self.user = User.objects.create(name="John",email='john@doe.com')
# 		self.music = Music.objects.create(title="hola",artist="John",album='languages')

# 	def test_add_favourite_music(self):
# 		"""
# 		Test wheter we can add a favourite music to an existing user.
# 		"""
# 		url = reverse('api_favourite_music',kwargs={'pk1':self.music.id,'pk2':self.user.id})
# 		response = self.client.put(url)
# 		self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

# class DeleteFavouriteMusicTest(APITestCase):
# 	def setUp(self):
# 		self.user = User.objects.create(name="John",email='john@doe.com')
# 		self.music = Music.objects.create(title="hola",artist="John",album='languages')

# 	def test_delete_favourite_music(self):
# 		"""
# 		Test wheter we can remove a favourite music from an existing user.
# 		"""
# 		url = reverse('api_favourite_music',kwargs={'pk1':self.music.id,'pk2':self.user.id})
# 		response = self.client.delete(url)
# 		self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)


