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

#### REST API:####

List users:

```GET /api/users ```

Get details from a user

```GET /api/user/<id> ```

Create a new user by sending a request with json data in the body of the request.{"name":"myname", "email":"myemail"} 

```POST /api/user/new``` 

Edit an existing user by sending a request with json data in the body of the request {"name":"newname", "email":"newemail"}. Partial updates are allowed.

```PUT /api/user/<id>/edit```

Delete an existing user.

```DELETE /api/user/<id>/delete``` 

List musics:

```GET /api/musics ```

Get details from a music.

```GET /api/music/<id> ```

Create a new music by sending a request with json data in the body of the request.{"title":"mytitle", "artist":"myartist", "album":"myalbum"}

```POST /api/music/new``` 

Edit an existing music by sending a request with json data in the body of the request {"title":"newtitle", "artist":"newartist", "album":"newalbum"}. Partial updates are allowed.

```PUT /api/music/<id>/edit```

Delete an existing music.

```DELETE /api/music/<id>/delete```

Add an existing music to the list of favourites from an existing user.

```PUT /api/music/<music_id>/user/user_id```

Delete a favourite music from the list of favourites from an existing user.

```DELETE /api/music/<music_id>/user/user_id```

####Live version:####

This project is available online at http://musicwallet.pythonanywhere.com/

####How to run locally:####

1 - Clone the repository:

	git clone https://github.com/AlexPnt/MusicWallet.git
	cd MusicWallet

2 - Install dependencies:

	pip install -r requirements.txt

3 - Setup the MySQL database

* Create a user "mysql"
* Create a database name "musicwallet_db" 

4 - Run migrations

	python manage.py migrate

5 - Populate the database
	
	python populate_db.py
6 - Run the server:
		
	python manage.py runserver --settings=musicwalletproject.settings.development

7 - Fire up your favourite browser and head to http://127.0.0.1:8000/musicwallet/ 

Enjoy your app !


	
	


