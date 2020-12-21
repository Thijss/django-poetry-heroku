# Settings

Inpired by [12factor](https://www.12factor.net/config), this project contains separate settings files for different environments.
The files are located in the `config.settings` module.

Additionally, in order to run the project, some environment variables need to be set.


## Environment variables

### DJANGO_SETTINGS_MODULE

Specifies which settings file to use:

* `config.settings.local`
* `config.settings.heroku`

### DEBUG
Specifies whether [Django's debug mode](https://docs.djangoproject.com/en/3.1/ref/settings/#debug) is turned on/off:
* `on`
* `off`

Never deploy a site into production with DEBUG turned `on`.


### DATABASE_URL
Specifies which database to connect to:
* `postgres://USER:PASSWORD@HOST:PORT/NAME`
* `sqlite:///PATH`

Using [django-environ](https://django-environ.readthedocs.io/en/latest/), the url is parsed to a specific database configuration.
Supporting databases can be found [here](https://django-environ.readthedocs.io/en/latest/#documentation).

### SECRET_KEY
Specifies [Django's secret key](https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-SECRET_KEY):
* Any string will do for local development
* For a production environment you can generate a key [here](https://djecrety.ir/)
