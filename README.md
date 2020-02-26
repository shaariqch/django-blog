# django-blog

A simple blog made using Django, following Django best practices and using Django built-in user authentication.

## Steps to run a dev server
### (optional, but recommended)
Create a virtual environment: `virtualenv env`
Activate environment: `env\Scripts\activate`

### Install dependencies
To install dependencies, run: `pip install -r requirements.txt`

### Model migrations 
Run model migrations:
```
python manage.py makemigrations
python manage.py migrate
```

### Run the server
Run: `python manage.py runserver`

If you want to use the admin panel, be sure to create a supseruser using the command `python manage.py createsuperuser` before starting the dev server.
