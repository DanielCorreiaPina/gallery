# gallery

gallery is a Python web app where the user can view, update and delete images from a gallery.

## Requirements

- Python 3
- Django
- PostgreSQL with gallery DB created
- Pillow (`pip install pillow`)

## Create Database

The current project settings assume that the DB user has being created as follows.

### Create User

To create the user run the following command on SQL Shell:

```SQL
create user gallery with password '12345678';
```

## Run it

Open the cmd on the root folder (where the manage.py is located) and execute the following commands:

```bash
>python manage.py migrate
>python manage.py runserver
```
