# ItemsPython

### A Django application for storing information about stuff in general.

This application is a web-based database which I (as of May 2016 "will") use to list my personal belongings. This is more like a personal django/python exercise.

### About the database

The database will be small and simple. At this moment django is configured to use the basic sqlite3 database, but will be changed to either postgresql or mysql in the future. (At least when the app is in "production".)

The database now consists of three tables: Item, Item_type and Maker. Item has one type and manyToMany relationship with Maker.

### About the project structure

I'm using virtualenv in this project. I will do the necessary scripts which can be used to set up the development environment. Basically on mac cli the commands given in the project root are: 
```shell
$ virtualenv --python=python3.5 ENV
$ source ENV/bin/activate
(ENV)$ pip install -r requirements.txt
```
The first command sets up the virtual environment with python3.5. (The python version defining might not be necessary.) The second command activates the virtualenv to be used as the project source. The last command installs all the pip-packages listed in the requirements.txt file (e.g. Django 1.9.6).

After setting up the development environment you will have to perform these commands in order to set up the database for use:
```shell
(ENV)$ cd itemdb
(ENV)$ python3 manage.py migrate
```

The virtual environment and database are in gitignore, so when this project is cloned into a new platform, the environment and the db have to be set up again. 

*TODO: list all dependencies*