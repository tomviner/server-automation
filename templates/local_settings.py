# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        # sudo apt-get install
        #    postgresql-9.3
        #    postgresql-server-dev-9.3
        #    postgresql-contrib-9.3
        # For new Databases:
        # psql -d template1 -c 'create extension hstore;'
        # For existing: ($ src/manage.py dbshell)
        # github_hook_collector=# create extension hstore;
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # https://help.ubuntu.com/community/PostgreSQL#Basic_Server_Setup
        # sudo -u postgres psql postgres
        # \password postgres
        'HOST':'localhost',
        'USER': 'projadm',
        'PASSWORD': 'qwerty',
        # createdb github_hook_collector
        'NAME': 'github_hook_collector',
    }
}

LOCAL_INSTALLED_APPS = (
    'django_extensions',
)
