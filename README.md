Favourite Music Management App/API 
===================================
MusicWallet is a Web App used to manage users and their favourite musics, exposing a REST API, built with Django and the Django Rest Framework.

#### Features (Web and REST API ):####
* Create/Read/Update/Delete users 
* Create/Read/Update/Delete musics 
* List users
* List musics
* Add favourite musics to an user
* List favourite musics of an user


####Requirements:####
* [Python 2.x](https://www.python.org/downloads/)
* [Django 1.10.2](https://www.djangoproject.com/download/)
* [Django REST framework](http://www.django-rest-framework.org/)
* [MySQL](http://www.mysql.com/)
* [mysqlclient](https://pypi.python.org/pypi/mysqlclient)

####Live version:####

This project is currently available at http://musicwallet.pythonanywhere.com/

#### REST API:####
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/ae565d7545fa44b5dd03)

Example calls made using the [httpie client](https://httpie.org):

List users:

```http GET http://musicwallet.pythonanywhere.com/api/users ```

Get details from a user

```http GET http://musicwallet.pythonanywhere.com/api/user/<id> ```

Create a new user by sending a request with json data in the body of the request.

```http --json POST http://musicwallet.pythonanywhere.com/api/user/new name="myname" email="myemail"``` 

Edit an existing user by sending a request with json data in the body of the request. Partial updates are allowed.

```http --json PUT http://musicwallet.pythonanywhere.com/api/user/<id>/edit name="newname" email="newemail"```

Delete an existing user.

```http DELETE http://musicwallet.pythonanywhere.com/api/user/<id>/delete``` 

List musics:

```http GET http://musicwallet.pythonanywhere.com/api/musics ```

Get details from a music.

```http GET http://musicwallet.pythonanywhere.com/api/music/<id> ```

Create a new music by sending a request with json data in the body of the request.

```http --json POST http://musicwallet.pythonanywhere.com/api/music/new title="mytitle" artist="myartist" album="myalbum"``` 

Edit an existing music by sending a request with json data in the body of the request. Partial updates are allowed.

```http --json PUT http://musicwallet.pythonanywhere.com/api/music/<id>/edit title="newtitle" artist="newartist" album="newalbum"```

Delete an existing music.

```http DELETE http://musicwallet.pythonanywhere.com/api/music/<id>/delete```

Add an existing music to the list of favourites from an existing user.

```http PUT http://musicwallet.pythonanywhere.com/api/music/<music_id>/user/<user_id>```

Delete a favourite music from the list of favourites from an existing user.

```http DELETE http://musicwallet.pythonanywhere.com/api/music/<music_id>/user/<user_id>```

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

6 - Run tests

	python manage.py test -v 2 --settings=musicwalletproject.settings.development

7 - Run the server:
		
	python manage.py runserver --settings=musicwalletproject.settings.development

8 - Fire up your favourite browser and head to http://127.0.0.1:8000/musicwallet/ 

Enjoy your app !


	
	





