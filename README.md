# Django-Poetry-Heroku

django-poetry-heroku is a project template for Django 3.1+ projects that are aimed to deploy at Heroku.
The project uses `poetry` for python packaging and dependency manangement.

## Prerequisities

- Python 3.6 or higher (https://www.python.org/downloads/)
- Poetry (https://python-poetry.org/docs/#installation)

## Usage
1. Clone the repository into `<your_project_name>_project`
    ```bash
    git clone git@github.com:Thijss/django-poetry-heroku.git <your_project_name>_project
    ```
2. Rename the folder `projectname` to `<your_project_name>`
    ```bash
    cd <your_project_name>_project
    mv projectname <your_project_name>
    ```
3. Review & update the info in `pyproject.toml`

4. Remove the git repo and start a new one.
    ```bash
    rm -rf .git
    git init
    git add .
    git commit -m "Initial commit"    
    ```

## Installation

1. Create and activate a virtualenv:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
2. Install requirements with `poetry`:
    ```bash
    poetry install
    ```

## Development
In order to run the project, some environment variables need to be set.
This project uses `django-environ`, which allows the use of a `.env` file to set environment variables.

To get started, copy the example file:
```bash
cp .env.example .env
```
Afterwards, open the `.env` file and change the file contents as you see fit.

You can find detailed descriptions of each variable in [SETTINGS](SETTINGS.md).

## Deployment (Heroku)


#### Heroku app
Make sure you've got a [Heroku account](https://signup.heroku.com/)
and a working [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install):
```bash
heroku login
```

Create your Heroku app:
```bash
heroku create <project_name>
```

Add required buildpacks for `poetry` and `python`:
```bash
heroku buildpacks:clear
heroku buildpacks:add https://github.com/moneymeets/python-poetry-buildpack.git
heroku buildpacks:add heroku/python
```

#### Database
Add a database to your Heroku app:
```bash
heroku addons:create heroku-postgresql:hobby-dev --name=<your_project_name>-pg
```

#### Environment variables
In order to run the project, some environment variables need to be set (see [SETTINGS](SETTINGS.md)).
```bash
heroku config:set DJANGO_SETTINGS_MODULE=config.settings.heroku
heroku config:set DEBUG=off
```
[Generate](https://djecrety.ir/) and set a secret key
```bash
heroku config:set SECRET_KEY=<generated_secret_key>
```

#### Deploy
Deploy your project:
```bash
git push heroku
```

You project should now be live!


## License
[MIT](LICENSE)