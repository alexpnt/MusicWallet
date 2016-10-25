Favourite Music Management App/API 
===================================
MusicWallet is a Web App used to manage users and their favourite musics, exposing a REST API, built with Django and the Django Rest Framework.

#### Features (Web and REST API ):####
* Users can sign up/sign in and delete their accounts 
* Users can edit their created musics
* Users may bookmark favourite musics
* Users may remove a music from their bookmarks


####Requirements:####
* [Python 2.x](https://www.python.org/downloads/)
* [Django 1.10.2](https://www.djangoproject.com/download/)
* [Django REST framework 3.5.0](http://www.django-rest-framework.org/)
* [MySQL](http://www.mysql.com/)
* [mysqlclient 1.3.9](https://pypi.python.org/pypi/mysqlclient)

####Live version:####

This project is currently available at http://musicwallet.pythonanywhere.com/

#### REST API:####
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/ae565d7545fa44b5dd03)

All requests must be signed against a user's username and password or use an authentication token (sent in the authorization header of the request). 

Example calls made using the [httpie client](https://httpie.org):

Obtaining the authentication token:

```http --json POST http://musicwallet.pythonanywhere.com/api-token-auth/  username=myuser password=mypassword```


List users:

```http GET http://musicwallet.pythonanywhere.com/api/users/ Authorization:"Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"```

Get details from a user

```http GET http://musicwallet.pythonanywhere.com/api/users/<id>/ Authorization:"Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"```

Edit an existing user by sending a request with json data in the body of the request.

```http --json PUT http://musicwallet.pythonanywhere.com/api/users/<id>/ username=newname email=newemail password=newpassword Authorization:"Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"```

Delete an existing user.

```http DELETE http://musicwallet.pythonanywhere.com/api/users/<id>/ Authorization:"Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"``` 

List musics:

```http GET http://musicwallet.pythonanywhere.com/api/musics/ Authorization:"Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"```

Get details from a music.

```http GET http://musicwallet.pythonanywhere.com/api/musics/<id>/ Authorization:"Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"```

Create a new music by sending a request with json data in the body of the request.

```http --json POST http://musicwallet.pythonanywhere.com/api/musics/ title=mytitle artist=myartist album=myalbum Authorization:"Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"``` 

Edit an existing music by sending a request with json data in the body of the request.

```http --json PUT http://musicwallet.pythonanywhere.com/api/musics/<id>/ title=newtitle artist=newartist album=newalbum Authorization:"Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"```

Delete an existing music.

```http DELETE http://musicwallet.pythonanywhere.com/api/musics/<id>/ Authorization:"Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"```

Add an existing music to the list of favourites from an existing user.

```http POST http://musicwallet.pythonanywhere.com/api/users/<music_id>/add_fav_music/ Authorization:"Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"```

Delete a favourite music from the list of favourites from an existing user.

```http DELETE http://musicwallet.pythonanywhere.com/api/users/<music_id>/remove_fav_music/ Authorization:"Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"```

####How to run locally:####

1 - Clone the repository:

	git clone https://github.com/AlexPnt/MusicWallet.git
	cd MusicWallet/musicwalletproject

2 - Install dependencies:

	pip install -r requirements.txt

3 - Setup the MySQL database

		mysql -uroot
		mysql>CREATE DATABASE musicwallet_db;
		mysql>CREATE USER 'mysql'@'localhost' IDENTIFIED BY 'mysql;
		mysql>GRANT ALL PRIVILEGES ON musicwallet_db.* TO 'mysql'@'localhost'; 
		mysql>FLUSH PRIVILEGES;
		mysql>quit

4 - Run migrations

	python manage.py migrate --settings=musicwalletproject.settings.development

5 - Populate the database with musics
	
	python populate_db.py

7 - Run the server:
		
	python manage.py runserver --settings=musicwalletproject.settings.development

8 - Fire up your favourite browser and head to:
        
    App - http://127.0.0.1:8000/musicwallet/
    API -   http://127.0.0.1:8000/api/

Enjoy your app !


	
	






