# reservations
Microservice for rent reservations mettings room


# For install

Change this fields in local_settings.py

<code>DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'DB',
        'USER': 'USER',
        'PASSWORD': 'PASSWORD',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}</code>

Create your environment 

install requirements with 
<code>pip install -r requirements.txt</code>

run <code>python manage.py makemigrations</code>

run <code>python manage.py migrate</code>

run <code>python manage.py runserver</code> 
