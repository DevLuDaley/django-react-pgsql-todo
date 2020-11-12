pipenv install psycopg2

# install psycopg2 to conect to postgres
    pipenv install psycopg2

# create new db using pgAdmin or pgsql cli 

# Update settings.py to include postgres instead of SQLite

By default, Django is configured to use SQLite as its backend. To use Postgres instead, “myproject/settings.py” needs to be updated:

# open myproject/settings.py
    cat myproject/settings.py
            or
    nano myproject/settings.py

original code to be replaced/changed
```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

```py
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': ‘<db_name>’,
        # 'USER': '<db_username>',
        # 'PASSWORD': '<password>',
        'HOST': '<db_hostname_or_ip>',
        'PORT': '<db_port>',
    }

}
```

for example
leave user and password blank until after we create the superuser account/object and set those fields.
```py
# setttings.py
...
import os
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        "NAME": "[developer_created_db_name]",
        # "USER": os.environ.get('DB_USER'),
        # "PASSWORD": os.environ.get('DB_PASS'),
        "HOST": "localhost",
        "PORT": "5432",
    }
}